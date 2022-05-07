from service import get_all_outdoor_activities

#print(get_all_outdoor_activities())


# [OutdoorActivities(id=1, outdoor_name='National Trust - Osterely Park and House', outdoor_address='Jersey Rd, Isleworth TW7 4RB, United Kingdom',
# outdoor_website='https://www.nationaltrust.org.uk/osterley-park-and-house', outdoor_image='1.jpeg',
# outdoor_descriptions="Stroll up the tree-lined drive, past the grazing Charolais cattle and you'd think you're in the country, not urban Hounslow. "
#                      "Surrounded by gardens, park and farmland, Osterley is one of the last surviving country estates in London.",
#                    outdoor_affordability='£13 - £20 - Depending on ticket type', outdoor_discount='10% off - show Sky badge'),



#
# <!--                    <img class="card-img-top" src="{{ url_for('static', filename='images/roses.jpeg') }} " alt="jinja name">-->
# <!--                         <img class="card-img-top" src="{{ url_for('static',filename='images/{{item.outdoor_image}}' ) }} " alt="{{ item.outdoor_name }}">-->
# <!--                     <img class="card-img-top" src="{{ url_for('static/images/{{item.outdoor_image}}' ) }} " alt="{{ item.outdoor_name }}">-->
# <!--                     <img class="card-img-top" src="{{ url_for('static', filename='{{item.outdoor_image}}' ) }} " alt="jinja name">-->
#
# # <!--                        working below: -->
# <!--                    <img class="card-img-top" src="{{ url_for('static', filename='images/roses.jpeg') }} " alt="jinja name">-->
