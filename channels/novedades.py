﻿# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# StreamOnDemand PureITA / XBMC Plugin
# Canale Novita
# http://www.mimediacenter.info/foro/viewtopic.php?f=36&t=7808
# ------------------------------------------------------------

from core import config
from core import logger
from core.item import Item

__channel__ = "novedades"
__category__ = "F"
__type__ = "generic"
__title__ = "Novedades"
__language__ = "IT"

DEBUG = config.get_setting("debug")


def isGeneric():
    return True


def mainlist(item, preferred_thumbnail="squares"):
    logger.info("[streamondemand-pureita novedades] mainlist")

    itemlist = [Item(channel=__channel__,
                     action="peliculas_movie",
                     title="Film",
                     thumbnail="https://raw.githubusercontent.com/orione7/Pelis_images/master/bannermenu/banner_movie_blueP2.png",
                     viewmode="movie"),
                Item(channel=__channel__,
                     action="series",
                     title="Serie TV",
                     thumbnail="https://raw.githubusercontent.com/orione7/Pelis_images/master/bannermenu/banner_tvshow_blueP2.png",
                     viewmode="movie"),
                Item(channel=__channel__,
                     action="peliculas_infantiles",
                     title="Cartoni Animati",
                     thumbnail="https://raw.githubusercontent.com/orione7/Pelis_images/master/bannermenu/banner_bambini_blueP2.png",
                     viewmode="movie"),
                Item(channel=__channel__,
                     action="anime",
                     title="Anime",
                     thumbnail="https://raw.githubusercontent.com/orione7/Pelis_images/master/bannermenu/banner_anime_blueP2.png",
                     viewmode="movie"),
                Item(channel=__channel__,
                     action="documentales",
                     title="Documentari",
                     thumbnail="https://raw.githubusercontent.com/orione7/Pelis_images/master/bannermenu/banner_documentary_blueP2.png",
                     viewmode="movie")]

    return itemlist


def peliculas_movie(item):
    logger.info("[streamondemand-pureita novedades] peliculas_movie")

    itemlist = []

    from channels import cineblog01
    item.url = "https://www.cb01.news/"
    itemlist.extend(cineblog01.peliculas(item))

    from channels import casacinema
    item.url = "https://www.casacinema.club/genere/film"
    itemlist.extend(casacinema.peliculas(item))	
	
    from channels import italiafilm
    item.url = "https://www.italia-film.io/novita-streaming-1/"
    itemlist.extend(italiafilm.peliculas(item))

    #from channels import piratestreaming
    #item.url = "http://www.piratestreaming.black/film-aggiornamenti.php"
    #itemlist.extend(piratestreaming.peliculas(item))

    #from channels import itafilmtv
    #item.url = "http://www.italia-film.gratis"
    #itemlist.extend(itafilmtv.peliculas(item))





    sorted_itemlist = []

    for item in itemlist:

        if item.extra != "next_page" and not item.title.startswith(">>"):
            item.title = item.title + " ([COLOR orange]" + item.channel.capitalize() + "[/COLOR])"
            sorted_itemlist.append(item)

    sorted_itemlist = sorted(sorted_itemlist, key=lambda Item: Item.title)

    return sorted_itemlist


def peliculas_infantiles(item):
    logger.info("[streamondemand-pureita novedades] peliculas_infantiles")

    itemlist = []

    import filmsenzalimiti_blue
    item.url = "https://filmsenzalimiti.gratis/category/film/animazione"
    itemlist.extend(filmsenzalimiti_blue.peliculas(item))
	
    import cinemalibero
    item.url = "https://www.cinemalibero.me/category/film-in-streaming/animazione/"
    itemlist.extend(cinemalibero.peliculas(item))
	
    import serietvu
    item.url = "https://www.serietvu.club/category/animazione-e-bambini/"
    itemlist.extend(serietvu.lista_serie(item))

    sorted_itemlist = []

    for item in itemlist:

        if item.extra != "next_page" and not item.title.startswith(">>"):
            item.title = item.title + " ([COLOR orange]" + item.channel.capitalize() + "[/COLOR])"
            sorted_itemlist.append(item)

    sorted_itemlist = sorted(sorted_itemlist, key=lambda Item: Item.title)

    return sorted_itemlist


def series(item):
    logger.info("[streamondemand-pureita novedades] series")

    itemlist = []
	


    #import serietvu
    #item.url = "http://www.serietvu.com/ultimi-episodi/"
    #itemlist.extend(serietvu.latestep(item))

    #import italiaserie
    #item.url = "http://www.italiaserie.co/"
    #itemlist.extend(italiaserie.peliculas(item))
	
    import filmsenzalimiti
    item.url = "https://filmsenzalimiti.bid/aggiornamenti-serie-tv/"
    itemlist.extend(filmsenzalimiti.peliculas_update(item))
	
    import serietvsubita
    item.url = "http://serietvsubita.net/"
    itemlist.extend(serietvsubita.peliculas_tv(item))
	
    import videotecaproject
    item.url = "https://www.videotecaproject.eu/serie-tv/"
    itemlist.extend(videotecaproject.pelis_new(item))
	
    #import thelordofstreaming
    #item.url = "http://www.thelordofstreaming.com/"
    #itemlist.extend(thelordofstreaming.peliculas_new(item))

    sorted_itemlist = []

    for item in itemlist:

        if item.extra != "next_page" and not item.title.startswith(">>"):
            item.title = item.title + " ([COLOR orange]" + item.channel.capitalize() + "[/COLOR])"
            sorted_itemlist.append(item)

    sorted_itemlist = sorted(sorted_itemlist, key=lambda Item: Item.title)

    return sorted_itemlist


def anime(item):
    logger.info("[streamondemand-pureita novedades] anime")

    itemlist = []

    import animesenzalimiti
    item.url = "https://animeleggendari.com/"
    itemlist.extend(animesenzalimiti.ultimiep(item))

    import animeforce
    item.url = "https://ww1.animeforce.org/"
    itemlist.extend(animeforce.ultimiep(item))

    sorted_itemlist = []

    for item in itemlist:

        if item.extra != "next_page" and not item.title.endswith(">>"):
            item.title = item.title + " ([COLOR orange]" + item.channel.capitalize() + "[/COLOR])"
            sorted_itemlist.append(item)

    sorted_itemlist = sorted(sorted_itemlist, key=lambda Item: Item.title)

    return sorted_itemlist


def documentales(item):
    logger.info("[streamondemand-pureita novedades] documentales")

    itemlist = []

    import documentari_dsda
    item.url = "https://documentari-streaming-da.com/?searchtype=movie&post_type=movie&sl=lasts&s="
    itemlist.extend(documentari_dsda.peliculas_tv(item))

    sorted_itemlist = []

    for item in itemlist:

        if item.extra != "next_page" and not item.title.startswith(">>"):
            item.title = item.title + " ([COLOR orange]" + item.channel.capitalize() + "[/COLOR])"
            sorted_itemlist.append(item)

    sorted_itemlist = sorted(sorted_itemlist, key=lambda Item: Item.title)

    return sorted_itemlist
