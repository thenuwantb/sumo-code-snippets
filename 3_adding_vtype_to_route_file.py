import pandas as pd
import os

# Change the directory
os.chdir(
    '<YOUR_FOLDER_PATH>')

# function to assign the time interval, so that the data frame can be later filtered based on that value
def assign_interval(number):
    if number < 900:
        return 900
    elif number < 1800:
        return 1800
    elif number < 2700:
        return 2700
    elif number < 3600:
        return 3600
    elif number < 4500:
        return 4500
    elif number < 5400:
        return 5400
    elif number < 6300:
        return 6300
    elif number < 7200:
        return 7200
    elif number < 8100:
        return 8100
    elif number < 9000:
        return 9000
    elif number < 9900:
        return 9900
    elif number < 10800:
        return 10800
    elif number < 11700:
        return 11700
    elif number < 12600:
        return 12600
    elif number < 13500:
        return 13500
    elif number < 14400:
        return 14400
    elif number < 15300:
        return 15300
    elif number < 16200:
        return 16200

# 1. Reading files
# 1.1. Route file in csv format
route_data_no_bus = pd.read_csv('1_2_random_routes_match_rda_counts_excluding_bus.csv')
# 1.2. Classified count
classified_count_data = pd.read_csv('RDA_Counts\\rda_classified_count_0530_1000_galle_road_colombo_entrance.csv')
# 2. Editing the file
# 2.1. Adding the time period
route_data_no_bus['time_period'] = route_data_no_bus['vehicle_depart'].map(assign_interval)
# 2.2. Insert 'vehicle_type' column as a blank column
route_data_no_bus['vehicle_type'] = ""
# 2.3. Splitting the dataframe with a random seed
rand_num = 45
routes_all_intervals = pd.DataFrame()

for index, row in classified_count_data.iterrows():
    three_wheeler_count = row['three_wheelers']
    motor_cycle_count = row['motor_cycles']
    car_count = row['car']
    van_count = row['van']
    large_bus_count = row['large_bus']
    mini_bus_count = row['mini_bus']
    light_goods_count = row['light_goods']
    medium_goods_count = row['medium_goods']
    heavy_goods_count = row['heavy_goods']
    multi_axel_count = row['multi_axel']

    route_data_from_interval = route_data_no_bus[route_data_no_bus['time_period'] == row['seconds']]

    if three_wheeler_count > 0:
        three_wheel_flow_interval = route_data_from_interval.sample(n=three_wheeler_count, replace=False,
                                                                    random_state=rand_num, axis=0)
        three_wheel_flow_interval['vehicle_type'] = 'three_wheel'
        route_data_from_interval = route_data_from_interval.drop(three_wheel_flow_interval.index)
        routes_all_intervals = routes_all_intervals.append(three_wheel_flow_interval)

    if motor_cycle_count > 0:
        motor_cycle_flow_interval = route_data_from_interval.sample(n=motor_cycle_count, replace=False,
                                                                    random_state=rand_num, axis=0)
        motor_cycle_flow_interval['vehicle_type'] = 'motor_cycle'
        route_data_from_interval = route_data_from_interval.drop(motor_cycle_flow_interval.index)
        routes_all_intervals = routes_all_intervals.append(motor_cycle_flow_interval)

    if car_count > 0:
        car_flow_interval = route_data_from_interval.sample(n=car_count, replace=False,
                                                            random_state=rand_num, axis=0)
        car_flow_interval['vehicle_type'] = 'car'
        route_data_from_interval = route_data_from_interval.drop(car_flow_interval.index)
        routes_all_intervals = routes_all_intervals.append(car_flow_interval)

    if van_count > 0:
        van_flow_interval = route_data_from_interval.sample(n=van_count, replace=False,
                                                            random_state=rand_num, axis=0)
        van_flow_interval['vehicle_type'] = 'van'
        route_data_from_interval = route_data_from_interval.drop(van_flow_interval.index)
        routes_all_intervals = routes_all_intervals.append(van_flow_interval)

    # if large_bus_count > 0:
    #     large_bus_flow_interval = route_data_from_interval.sample(n=large_bus_count, replace=False,
    #                                                               random_state=rand_num, axis=0)
    #     large_bus_flow_interval['vehicle_type'] = 'large_bus'
    #     route_data_from_interval = route_data_from_interval.drop(large_bus_flow_interval.index)
    #     routes_all_intervals = routes_all_intervals.append(large_bus_flow_interval)

    # if mini_bus_count > 0:
    #     mini_bus_flow_interval = route_data_from_interval.sample(n=mini_bus_count, replace=False,
    #                                                              random_state=rand_num, axis=0)
    #     mini_bus_flow_interval['vehicle_type'] = 'mini_bus'
    #     route_data_from_interval = route_data_from_interval.drop(mini_bus_flow_interval.index)
    #     routes_all_intervals = routes_all_intervals.append(mini_bus_flow_interval)

    if light_goods_count > 0:
        light_goods_flow_interval = route_data_from_interval.sample(n=light_goods_count, replace=False,
                                                                    random_state=rand_num, axis=0)
        light_goods_flow_interval['vehicle_type'] = 'light_goods'
        route_data_from_interval = route_data_from_interval.drop(light_goods_flow_interval.index)
        routes_all_intervals = routes_all_intervals.append(light_goods_flow_interval)

    if medium_goods_count > 0:
        medium_goods_flow_interval = route_data_from_interval.sample(n=medium_goods_count, replace=False,
                                                                     random_state=rand_num, axis=0)
        medium_goods_flow_interval['vehicle_type'] = 'medium_goods'
        route_data_from_interval = route_data_from_interval.drop(medium_goods_flow_interval.index)
        routes_all_intervals = routes_all_intervals.append(medium_goods_flow_interval)

    if heavy_goods_count > 0:
        heavy_goods_flow_interval = route_data_from_interval.sample(n=heavy_goods_count, replace=False,
                                                                    random_state=rand_num, axis=0)
        heavy_goods_flow_interval['vehicle_type'] = 'heavy_goods'
        route_data_from_interval = route_data_from_interval.drop(heavy_goods_flow_interval.index)
        routes_all_intervals = routes_all_intervals.append(heavy_goods_flow_interval)

    if multi_axel_count > 0:
        multi_axel_flow_interval = route_data_from_interval.sample(n=multi_axel_count, replace=False,
                                                                   random_state=rand_num, axis=0)
        multi_axel_flow_interval['vehicle_type'] = 'multi_axel'
        route_data_from_interval = route_data_from_interval.drop(multi_axel_flow_interval.index)
        routes_all_intervals = routes_all_intervals.append(multi_axel_flow_interval)

routes_all_intervals.sort_values(by='vehicle_depart', ascending=True, inplace=True)
routes_all_intervals.to_csv('1_3_routes_matching_classifed_counts_no_bus.csv')

## Write to an xml so that SUMO can understand

data_to_write_rou_xml = pd.read_csv('1_3_routes_matching_classifed_counts_no_bus.csv')

# Opening the xml and writing the starting section of the xml
fh = open("1_4_matching_vehicle_types_to_match_RDA_counts.rou.xml", 'w')

fh.write(
    '<routes xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/routes_file.xsd">\n')

# from P.S. Bokare et al. : Acceleration-Deceleration Behaviour of Various Vehicle Types (only three wheel value is taken)
fh.write('\t<vType id="three_wheel" accel="0.6" decel="1.14" color="0,0,1" length="2.55" width="1.55" '
         'carFollowModel="Krauss" minGap="2.5" sigma="0.5" tau="1.0" lcSpeedGain="1.0"/>\n')
fh.write(
    '\t<vType id="motor_cycle" color="1,0,1" length="2.0" width="0.9" vClass="moped" carFollowModel="Krauss" '
    'minGap="2.5" sigma="0.5" tau="1.0" lcSpeedGain="1.0"/>\n')
fh.write('\t<vType id="car" vClass="passenger" length="4.2" width="2.12" carFollowModel="Krauss" minGap="2.5" '
         'sigma="0.5" tau="1.0" lcSpeedGain="1.0"/>\n')  # Sedan car
fh.write('\t<vType id="van"  color="0.70,0.52,0.75" length="5.3" width="2.10" vClass="passenger" guiShape= '
         '"passenger/van" carFollowModel="Krauss" minGap="2.5" sigma="0.5" tau="1.0" lcSpeedGain="1.0"/>\n')
# from P.S Bokare et al. took the max acceleration for a Truck, as bus acceleration values are not
# mentioned
fh.write('\t<vType id="large_bus" accel="1.0" decel="0.88" color="0.23,0.48,0.34" length="10.80" width="2.95" '
         'vClass="bus" carFollowModel="Krauss" minGap="2.5" sigma="0.5" tau="1.0" lcSpeedGain="1.0"/>\n')
fh.write('\t<vType id="mini_bus" color="0.23,0.48,0.34" length="7.01" width="2.36" vClass="bus" '
         'carFollowModel="Krauss" minGap="2.5" sigma="0.5" tau="1.0" lcSpeedGain="1.0"/>\n')
fh.write('\t<vType id="light_goods" color="1.00,0.49,0.00" length="3.70" width="1.85" vClass="truck" '
         'carFollowModel="Krauss" minGap="2.5" sigma="0.5" tau="1.0" lcSpeedGain="1.0"/>\n')
fh.write('\t<vType id="medium_goods" color="1.00,0.49,0.00" length="6.25" width="2.35" vClass="truck" '
         'carFollowModel="Krauss" minGap="2.5" sigma="0.5" tau="1.0" lcSpeedGain="1.0"/>\n')
fh.write('\t<vType id="heavy_goods" color="1.00,0.49,0.00" length="8.48" width="3.02" vClass="truck" '
         'carFollowModel="Krauss" minGap="2.5" sigma="0.5" tau="1.0" lcSpeedGain="1.0"/>\n')
fh.write('\t<vType id="multi_axel" color="1.00,0.49,0.00" length="15.50" width="3.10" vClass="trailer" '
         'carFollowModel="Krauss" minGap="2.5" sigma="0.5" tau="1.0" lcSpeedGain="1.0"/>\n')

for index, row in data_to_write_rou_xml.iterrows():
    vehicle_depart = row['vehicle_depart']
    vehicle_id = row['vehicle_id']
    route_edges = row['route_edges']
    vehicle_type = row['vehicle_type']

    fh.write('\t<vehicle id="{}" type="{}" depart="{}" departLane="free" departPos="free" departSpeed="max">\n'.format(vehicle_id, vehicle_type, vehicle_depart))
    fh.write('\t\t<route edges="{}"/>\n'.format(route_edges))
    fh.write('\t</vehicle>\n')

fh.write('</routes>')
fh.close()


