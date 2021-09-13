clear
close all

status = system("scp raspi:~/bme280/data.csv data.csv");

filename = 'data.csv';
data = readcell(filename);

time = datetime(string((data(:, 1))));
temp = cell2mat(data(:, 2));
humi = cell2mat(data(:, 3));
pres = cell2mat(data(:, 4));

f = figure;
f.Position(2:4) = [200 750 750];
fs = 12;
n = 3;
subplot(n, 1, 1)
plot(time, temp, '-ok')
str =...
    strcat(string(min(month(time))), "/", string(max(day(time))-1),...
    "                                        Time                                         ",...
    string(max(month(time))), "/", string(max(day(time))));
xlabel(str)
xlim([time(end)-hours(24) time(end)])
xticks(time)
xticklabels(string(hour(time)))
ylabel('Temperature in degree')
ylim([-10 40])
grid on
set(gca, 'FontSize', fs)

subplot(n, 1, 2)
plot(time, humi, '-ok')
xlabel(str)
xlim([time(end)-hours(24) time(end)])
xticks(time)
xticklabels(string(hour(time)))
ylabel('Humidity in %')
ylim([40 90])
grid on
set(gca, 'FontSize', fs)

subplot(n, 1, 3)
plot(time, pres, '-ok')
xlim([time(end)-hours(24) time(end)])
xticks(time)
xticklabels(string(hour(time)))
xlabel(str)
ylabel('Pressure in hPa')
ylim([1000 1020])
grid on
set(gca, 'FontSize', fs)