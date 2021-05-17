import subprocess
import os

os.chdir('<YOUR_FOLDER_PATH')

command_sumo = 'sumo -c osm.sumocfg --vehroute-output 1_vehroutes_random_trips_galle_road.xml'

command_route_sampler = 'routeSampler.py -r 1_vehroutes_random_trips_galle_road.xml --edgedata-files rda_counts_2019_dehiwala.xml ' \
          ' -o 1_random_routes_match_rda_counts.rou.xml '

command_xml_2_csv = 'xml2csv.py 1_random_routes_match_rda_counts_excluding_bus.rou.xml -s , -o 1_2_random_routes_match_rda_counts_excluding_bus.csv'

subprocess.run(command_sumo, shell=True)
subprocess.run(command_route_sampler, shell=True)
subprocess.run(command_xml_2_csv, shell=True)
