#!/bin/bash

set -e

export FB_ACCESS_TOKEN=${FB_ACCESS_TOKEN:-'EAACEdEose0cBAKc9T1rq9ux2V1PbFFf86JZCOV1XmV4NobAXqUXZA7U9F1UaaOdQZABvz73030MJoC3gGoQrE8IEoMl4gF4rgaJ2VHDwmrHCrofZCskZA6MmQadlJQBqtRsgIcIhtelIJOJoBHBr5vBoOGZCC6boeekmZAvl9jEWwZDZD'}
export OUTPUT_FOLDER=${OUTPUT_FOLDER:-'./data_raw'}

# right-wing and pro-PP groups
facebook_groups_right=(
    # PRIVATE GROUPS
    '1440040859633182' # Yo soy del PP
    '1642017206049931' # DONDE TIENEN QUE ESTAR: EN LA OPOSICION
    '471789886337362'  # LOS ESPAÑOLES PRIMERO Y ANTE TODO NUESTROS DERECHOS
    '1683276048570203' # POR UNA DERECHA MUCHO MÁS UNIDA
    '1580929135456551' # TODOS CON EL PP, POR ESPAÑA Y LA LIBERTAD.
    '117306734950207'  # YO voto al partido POPULAR
    '850574101682653'  # Yo siempre estaré con el PP
    '1676778442561884' # Apoyemos al Sr Mariano Rajoy Brey
    '1562926630633052' # VOX Afiliados y Simpatizantes
    '103792330485'     # Amigos de Federico Jiménez Losantos
    '2405115129'       # COPE

    # PUBLIC GROUPS
    '1645005842401567' # Diario de una alcaldesa incompetente
    '429815277205101'  # Todos con Xavi García Albiol
    '356343377870396'  # MOLESTA A PODEMOS
)

# left-wing and pro-Podemos groups
facebook_groups_left=(
    # PRIVATE GROUPS
    '854571741255544'  # PODEMOS SOMOS TODOS
    '1649529275260256' # Seguidores de Iñigo Errejón, Pablo Iglesias... Unidos Podemos!
    '929304267188878'  # PODEMOS PARA LA GENTE
    '1509217819340568' # MI VOTO ES PARA PODEMOS
    '1760459347545421' # UNIDOS PODEMOS CAMBIAR ESPAÑA

    # PUBLIC GROUPS
    '270567806468987'  # YO ESTOY Y VOTO A  ¡ ¡ ¡ PODEMOS ! ! !
    '1278667078814901' # UNIDOS PODEMOS. PRESIDENTE PABLO IGLESIAS
    '507243119456188'  # Amigos a los que les gusta Podemos
    '335463566624041'  # PODEMOS ES LA OPOSICION
    '1573767572931072' # " PoR eL CaMBio ".  ¡¡ Unidos Podemos !!
    '1432908763665732' # Por ESPAÑA si que PODEMOS
)

for i in ${facebook_groups_right[@]}; do
    python crawler.py $i 'right'
done

for i in ${facebook_groups_left[@]}; do
    python crawler.py $i 'left'
done

exit 0