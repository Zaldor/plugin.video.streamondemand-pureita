# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# streamondemand.- XBMC Plugin
# Canal para scambiofile
# http://www.mimediacenter.info/foro/viewforum.php?f=36
# ------------------------------------------------------------
import re
import urllib
import urlparse

from core import config
from core import logger
from core import scrapertools
from core.item import Item
from core.tmdb import infoSod

__channel__ = "scambiofile"
__category__ = "F"
__type__ = "generic"
__title__ = "Scambiofile (IT)"
__language__ = "IT"

DEBUG = config.get_setting("debug")

site = "http://scambiofile.io"


def isGeneric():
    return True


def mainlist(item):
    logger.info("streamondemand.scambiofile mainlist")
    itemlist = [Item(channel=__channel__,
                     title="[COLOR azure]Novità-Film .torrent stream[/COLOR]",
                     action="peliculas",
                     url="%s/browse.php?cat=1" % site,
                     thumbnail="https://raw.githubusercontent.com/orione7/Pelis_images/master/channels_icon_pureita/popcorn_cinema_P.png"),
                Item(channel=__channel__,
                     title="[COLOR yellow]Cerca...[/COLOR]",
                     action="search",
                     extra="torrent",
                     thumbnail="https://raw.githubusercontent.com/orione7/Pelis_images/master/channels_icon_pureita/search_P.png")]

    return itemlist


def search(item, texto):
    logger.info("[scambiofile.py] " + item.url + " search " + texto)
    item.url = "http://www.scambiofile.io/browse.php?cat=1&search=" + texto
    try:
        return peliculas(item)
    # Se captura la excepción, para no interrumpir al buscador global si un canal falla
    except:
        import sys
        for line in sys.exc_info():
            logger.error("%s" % line)
        return []


def peliculas(item):
    logger.info("streamondemand.scambiofile peliculas")
    itemlist = []

    # Descarga la pagina
    data = scrapertools.cache_page(item.url, timeout=10)

    # Extrae las entradas (carpetas)
    patron = '<a <td align="left">[^)]+.[^)]+.[^=]+=\'(.*?)\' target=\'_blank\'>(.*?)</a>'
    matches = re.compile(patron, re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedurl, scrapedtitle in matches:
        scrapedtitle = scrapertools.decodeHtmlentities(scrapedtitle)
        url = scrapedurl
        url = url.replace("%2F", "/")
        url = url.replace("%3F", "?")
        url = url.replace("%26n%3", "&n=")
        url = url.replace("/details.php", "http://www.scambiofile.io/details.php")
        scrapedplot = ""
        scrapedthumbnail = ""
        if (DEBUG): logger.info("title=[" + scrapedtitle + "], url=[" + url + "], thumbnail=[" + scrapedthumbnail + "]")
        itemlist.append(infoSod(
            Item(channel=__channel__,
                 action="play",
                 fulltitle=scrapedtitle,
                 show=scrapedtitle,
                 title="[COLOR darkkhaki].torrent [/COLOR]""[COLOR azure]" + scrapedtitle + "[/COLOR]",
                 url=url,
                 thumbnail=scrapedthumbnail,
                 plot=scrapedplot,
                 folder=True), tipo='movie'))

    # Extrae el paginador
    patronvideos = '<td class="highlight"><b>[^h]+href="([^"]+)"[^>]+>'
    matches = re.compile(patronvideos, re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    if len(matches) > 0:
        url = urlparse.urljoin(item.url, matches[0])
        url = url.replace("&amp;", "&")
        itemlist.append(
            Item(channel=__channel__,
                 action="peliculas",
                 title="[COLOR orange]Successivo>>[/COLOR]",
                 url=url,
                 thumbnail="https://raw.githubusercontent.com/orione7/Pelis_images/master/vari/successivo_P.png",
                 folder=True))

    return itemlist


def play(item):
    logger.info("[scambiofile.py] play")
    itemlist = []

    data = scrapertools.cache_page(item.url)

    patron = '<a class=\'btn btn-warning small\' href="(magnet[^&]+)[^>]+>'
    patron = urllib.unquote(patron).decode('utf8')
    link = scrapertools.find_single_match(data, patron)
    link = urlparse.urljoin(item.url, link)

    itemlist.append(
        Item(channel=__channel__,
             action=play,
             server="torrent",
             title=item.title,
             url=link,
             thumbnail=item.thumbnail,
             plot=item.plot,
             folder=False))

    return itemlist
