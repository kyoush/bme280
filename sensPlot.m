clear
close all

status = system("scp raspi:~/bme280/data.csv data.csv");

filename = 'data.csv';
A = readcell(filename);

time = A{:, 1};
temp = A{:, 2};
humi = A{:, 3};
pres = A{:, 4};