# The idea of creating this script is to insert busses as realistically as possible to the simulation
# 1. Add the vehicle according to the time stamp (-10 sec offset) based on the cctv footages
# 2. Stopping times at the stations are random

# import necessary packages
import pandas as pd
import numpy as np


# functions
def stopping_duration(bus_type, list_long_dist, list_short_dist):
    rand_int = np.random.randint(0, 99)
    if bus_type == "BUS_SD":
        return list_short_dist[rand_int]

    elif bus_type == "BUS_LD":
        return list_long_dist[rand_int]
    elif bus_type == "BUS_O":
        return "0"


# Values to be used for busses
bus_max_speed_short_distance = "40"
bus_max_speed_long_distance = "70"
bus_max_speed_other = "50"

bus_route_cross_junc_kollupitiya = "112446385#5 112446385#6 112446385#7 112446385#8 112446385#9 199382592#0 199382592#1 " \
                                   "199382592#2 199382592#3 199382592#4 199382592#5 199382592#6 199382592#7 " \
                                   "199382592#8 112446386#1 112446386#2 112446386#4 112446386#5 112446386#6 " \
                                   "112446386#7 112446386#8 112446386#11 112446386#12 gneE1 gneE2 gneE3 " \
                                   "112446377#0.49 112446377#1 112446377#2 102650972#0 102650972#1 102651364#0 " \
                                   "102651364#1 102651364#2 102651364#3 102651364#4 102651364#5 102651364#6 " \
                                   "102651364#7 102651364#8 102651364#9 102651364#10 102651364#11 102651364#12 " \
                                   "102651364#14 102651364#15 102651364#16 102651364#17 102651364#18 102651364#19 " \
                                   "102651364#20 gneE10 gneE49 gneE14 102651364#23.9 758636097#0 758636097#1 " \
                                   "758636097#3 758636097#4 758636097#6 758636097#7 758636097#8 758636097#9 " \
                                   "758636097#10 758636097#11 758636097#12 758636097#14 758636097#15 758636097#16 " \
                                   "758636097#17 758636097#18 758636097#19 758636097#20 758636097#22 758636097#23 " \
                                   "758636097#24 758636097#25 758636097#26 758636097#27 194092438#0 194092438#1 " \
                                   "194092438#2 194092438#3 194092438#4 194092438#5 194092438#6 194092438#7 " \
                                   "48701240#1 48701240#4 48701240#5 48701240#6 48701240#7 48701240#8 48701240#9 " \
                                   "48701240#11 48701240#12 48701240#13 48701240#14 48701240#15 48701240#16 " \
                                   "48701240#17 48701240#17.68 50071260#1 50071260#2 50071260#3 50071260#4 gneE40 " \
                                   "50071266#1 50071266#2 50071266#3 50071266#4 50071266#5 50071266#6 50071266#7 " \
                                   "50071266#8 50071266#9 50071266#10 50071266#11 50071266#12 50071266#13 50071266#14 " \
                                   "50071266#15 50071266#16 50071266#17 50071266#18 50071266#19 50071266#20 " \
                                   "50071266#21 50071266#22 50071266#24 98371177 161480084#0 161480084#1 161480084#2 " \
                                   "161480084#3 161480084#4 161480084#5 161480084#6 161480084#7 161480084#8 " \
                                   "161480084#9 161480084#10 161480084#11 161480084#12 161480084#14 161480084#15 " \
                                   "161480084#16 161480084#17 161480084#18 161480084#19 161480084#20 161480084#22 " \
                                   "161480084#23 161480084#24 161480084#25 161480084#26 356578614 24791907 24791916#1 " \
                                   "24791916#2 24791916#3 24791916#5 24791916#6 24791916#8 24791916#10 24791916#12 " \
                                   "377515219#0 377515219#1 377515219#2 377515219#3 377515219#4 377515219#5 " \
                                   "377515219#6 377515219#7 377515219#8 377515219#9 377515219#11 377515219#13 " \
                                   "377515219#15 377515219#16 377515219#17 377515219#18 377515220#1 377515220#3 " \
                                   "377515220#4 356319332#0 356319332#2 356319332#5 356319332#6 356319332#7 " \
                                   "356319332#8 356319332#10 356319332#11 356319332#12 356319332#15 356319332#16 " \
                                   "356319332#17 356319332#18 356319332#20 356319332#21 52322536#0 52322536#2 " \
                                   "52322536#3 52322536#5 52322536#6 52322536#7 52322536#8 52322536#9 52322536#10 " \
                                   "52322536#12 52322536#14 52322536#15 52322536#16 52322536#17 52322536#18 " \
                                   "52322536#19 52322536#20 52322536#21 52322536#22 52322536#23 52322536#24 " \
                                   "52322536#25 52322536#26 52322536#27 52322536#28 52322536#29 52322536#30 " \
                                   "52322536#31 52322536#32 52322536#33 356319069#1 356319069#3 356319069#4 " \
                                   "356319069#5 356319069#6 356319069#7 356319069#8 356319069#9 356319069#10 " \
                                   "356319069#11 356319069#13 356319069#15 356319069#17 356319069#18 359947709#2 " \
                                   "359947709#3 359947709#4 289027979 455043526 455043517 455043472 455043449 " \
                                   "455043369#2 455043345 53473737#1 455043325 455043168 455043315#1 98371210 " \
                                   "18599046#6 18598833#0 10548280#8 10548280#1 10548280#3 10548283 10590157#0 10590157#1"


# open data files

# 1. Open ordered bus stops
ordered_bus_stops = pd.read_csv('bus_related\\ordered_bus_stops_galle_road.csv')

# 2. Open video footage based bus count (to get the departure time and type of the bus)
bus_type_dep_time = pd.read_csv('bus_related\\cctv_footage_survey_bus_count.csv')

# Create random stopping times
long_distance_bus_stoping_time = np.random.normal(15, 5, 100).tolist()
short_distance_bus_stopping_time = np.random.normal(20, 10, 100).tolist()

long_distance_bus_stoping_time_formatted = [0 if x < 0 else x for x in long_distance_bus_stoping_time]
short_distance_bus_stopping_time_formatted = [0 if x < 0 else x for x in short_distance_bus_stopping_time]

long_distance_bus_stoping_time_formatted = ['%.0f' % elem for elem in long_distance_bus_stoping_time_formatted]
short_distance_bus_stopping_time_formatted = ['%.0f' % elem for elem in short_distance_bus_stopping_time_formatted]

print(long_distance_bus_stoping_time_formatted)

print(long_distance_bus_stoping_time_formatted)
# open the file and starting to write
with open('2_bus_flows_and_stops.add.xml', 'w') as fh:
    fh.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    fh.write(
        '<additional xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/additional_file.xsd">\n')
    fh.write('\n')

    fh.write("""\t<busStop id="bambalapitiya_flats" lane="377515219#1_0" startPos="40.00" endPos="50.00" name="Bambalapitiya Flats" friendlyPos="1"/>
    <busStop id="belek_kade" lane="102651364#14_0" startPos="260.00" endPos="276.00" name="Belek Kade Junction" friendlyPos="1"/>
    <busStop id="cagills_bank" lane="52322536#7_0" startPos="2.00" endPos="12.00" name="Cargilla Bank Halt"/>
    <busStop id="commercial_bank_rw" lane="112446386#6_0" startPos="58.96" endPos="74.96" name="Commercial Bank Halt"/>
    <busStop id="crescat" lane="455043325_0" startPos="12.00" endPos="22.00" name="Crescat Halt"/>
    <busStop id="cross_junction" lane="199382592#0_0" startPos="67.26" endPos="83.26" name="Cross Junction" friendlyPos="1"/>
    <busStop id="dehiwala_junc" lane="gneE40_0" startPos="5.00" endPos="29.00" name="Dehiwala Junction" friendlyPos="1"/>
    <busStop id="dhramarama_temp" lane="758636097#3_0" startPos="29.00" endPos="45.00" name="Dharmarama Temple Road Halt" friendlyPos="1"/>
    <busStop id="galle_face_1" lane="18598833#0_0" startPos="25.00" endPos="41.00" name="Galle Face Halt 1" friendlyPos="1"/>
    <busStop id="galle_face_2" lane="18598833#0_0" startPos="515.00" endPos="525.00" name="Galle Face Halt 2"/>
    <busStop id="german_tec" lane="102650972#0_0" startPos="134.00" endPos="150.00" name="German Tec Halt"/>
    <busStop id="golumadama" lane="102651364#4_0" startPos="8.00" endPos="24.00" name="Golumadama Halt"/>
    <busStop id="golumadama_sathosa" lane="102651364#10_0" startPos="60.00" endPos="70.00" name="Golumadama Sathosa Halt" friendlyPos="1"/>
    <busStop id="hotel_road" lane="48701240#1_0" startPos="6.00" endPos="16.00" name="Hotel Road Halt" friendlyPos="1"/>
    <busStop id="katubedda_junc" lane="gneE1_0" startPos="6.00" endPos="32.00" name="Katubedda Junction" friendlyPos="1"/>
    <busStop id="kollupitiya_junc" lane="359947709#2_0" startPos="5.00" endPos="19.00" name="Kollupitiya Junction Halt"/>
    <busStop id="lakshapathiya" lane="112446386#4_0" startPos="244.48" endPos="260.48" name="Lakshapathiya"/>
    <busStop id="magestic_city" lane="356319332#16_0" startPos="10.00" endPos="34.00" name="Majestic City Halt"/>
    <busStop id="maliban_junc" lane="gneE49_0" startPos="5.00" endPos="29.00" name="Maliban Junction Halt" friendlyPos="1"/>
    <busStop id="mallika_bakery" lane="112446377#1_0" startPos="57.00" endPos="73.00" name="Mallika Bekariya Halt" friendlyPos="1"/>
    <busStop id="marino_mall" lane="52322536#16_0" startPos="4.00" endPos="14.00" name="Marino Mall Halt" friendlyPos="1"/>
    <busStop id="mendis_tower" lane="199382592#4_0" startPos="23.71" endPos="47.71" name="Mendis Tower Hall" friendlyPos="1"/>
    <busStop id="milagiriya" lane="377515220#1_0" startPos="12.00" endPos="22.00" name="Milagiriya" friendlyPos="1"/>
    <busStop id="mount_lavinia_court" lane="194092438#3_0" startPos="58.25" endPos="68.25" name="Mount Lavinia Magistrate Court" friendlyPos="1"/>
    <busStop id="mount_lavinia_junc" lane="758636097#26_0" startPos="114.78" endPos="121.61" name="Mount Lavinia Junction" friendlyPos="1"/>
    <busStop id="mount_lavinia_police" lane="758636097#9_0" startPos="76.00" endPos="86.00" name="Mount Lavinia Police Station Halt" friendlyPos="1"/>
    <busStop id="odeon_cinema" lane="48701240#9_0" startPos="5.00" endPos="15.00" name="Odeon Cinema"/>
    <busStop id="pan_asia" lane="52322536#31_0" startPos="2.00" endPos="12.00" name="Kollupitiya Pan Asia Bank Halt" friendlyPos="1"/>
    <busStop id="ratmalana_depot" lane="758636097#12_0" startPos="58.00" endPos="67.00" name="Ratmalana CTB Depot" friendlyPos="1"/>
    <busStop id="rawatawatta" lane="199382592#8_0" startPos="10.00" endPos="45.00" name="Rawatawatta"/>
    <busStop id="roxi_cinema" lane="161480084#2_0" startPos="18.00" endPos="34.00" name="Roxi Film Hall Halt" friendlyPos="1"/>
    <busStop id="savoy_cinema" lane="161480084#25_0" startPos="36.00" endPos="46.00" name="Savoy Cinema" friendlyPos="1"/>
    <busStop id="soyza_flat" lane="102651364#0_0" startPos="104.00" endPos="120.00" name="Soyza Flat Halt"/>
    <busStop id="st_peters" lane="24791916#6_0" startPos="1.00" endPos="7.92" name="St. Peters College Halt" friendlyPos="1"/>
    <busStop id="vijitha_hall" lane="102651364#17_0" startPos="20.00" endPos="45.00" name="Vijitha Film Hall Halt" friendlyPos="1"/>
    <busStop id="vogue_jewel" lane="52322536#24_0" startPos="5.00" endPos="15.00" name="Vogue Jewellers Halt" friendlyPos="1"/>
    <busStop id="waydya_rd" lane="50071266#9_0" startPos="8.00" endPos="24.00" name="Waydya Road Halt" friendlyPos="1"/>
    <busStop id="wellawatta_arpico" lane="161480084#7_0" startPos="30.00" endPos="40.00" name="Wellawatte Arpico Halt"/>
    <busStop id="wellawatta_mosque" lane="161480084#22_0" startPos="94.00" endPos="110.00" name="Wellawatta Mosque" friendlyPos="1"/>
    <busStop id="wellawatta_police" lane="161480084#17_0" startPos="34.00" endPos="50.00" name="Wellawatte Police Station Halt"/>
    <busStop id="william_junc" lane="50071266#17_0" startPos="30.00" endPos="46.00" name="Willium Junction" friendlyPos="1"/>
    """)
    fh.write('\n')

    # short distance bus type
    fh.write(
        '\t<vType id="BUS_SD" vClass="bus" accel="2.6" decel="4.5" sigma="0.9" length="12" minGap="3" maxSpeed="{}" color="red" '
        'guiShape="bus"/>\n'.format(bus_max_speed_short_distance))

    # long distance bus type
    fh.write('\t<vType id="BUS_LD" vClass="bus" accel="2.6" decel="4.5" sigma="0.9" length="12" minGap="3" maxSpeed="{}" '
             'color="blue" guiShape="bus"/>\n'.format(bus_max_speed_long_distance))

    fh.write('\t<vType id="BUS_O" vClass="bus" accel="2.6" decel="4.5" sigma="0.9" length="10" minGap="3" maxSpeed="{}" '
             'color="yellow" guiShape="bus"/>\n'.format(bus_max_speed_other))
    fh.write('\n')

    # reading bus by bus and insert to the additional file

    for index_o, row_o in bus_type_dep_time.iterrows():
        vehicle_depart = row_o['time_enter_simulation']
        type = row_o['bus_type_code']
        id = row_o['vehicle_id']

        fh.write('\t<vehicle id="{}" type="{}" depart="{}">\n'.format(id, type, vehicle_depart))

        fh.write('\t\t<route edges="{}"/>\n'.format(bus_route_cross_junc_kollupitiya))

        for index_1, row_1 in ordered_bus_stops.iterrows():
            # if index_1 == 10:
            #     break
            bus_stop = row_1['stop_name']
            duration = stopping_duration(type, long_distance_bus_stoping_time_formatted,
                                         short_distance_bus_stopping_time_formatted)

            fh.write('\t\t<stop busStop="{}" duration="{}"/>\n'.format(bus_stop, duration))

        fh.write('\t</vehicle>\n')
    fh.write('</additional>\n')

