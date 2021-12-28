%本程序用于分析每个电压下两个通道的信号峰值、下降沿时间的直方图高斯拟合，以及每个电压下两个通道的符合百分比
%使用者只需要修改电压、通道和路径信息即可
%结果中mu、sig为高斯分布的两个参数，muci、sigmaci为置信区间
clear all;
voltage = [700,850,1000];%选取的3个电压
ch = [1,2];%选取的两个通道,把触发通道写在前面
s1 = 'C:\Users\11254\Desktop\output_';
s2 = '\output-CH';
s3 = '-';
s4 = '.csv';%文件路径是C:\Users\11254\Desktop\output_700\output-CH1-0.csv
for voltage_i = 1:3
    fuhe(voltage_i) = 0;
    for ch_i = 1:2
        for j = 0: 999
            s=strcat(s1,num2str(voltage(voltage_i)),s2,num2str(ch(ch_i)),s3,num2str(j),s4);
            data_transposition = csvread(s,1,0);
            data = [data_transposition'];
            time_data = data(1,:);
            voltage_data = data(2,:);
            basic_sum = 0;
            for basic_i = 1:200
                basic_sum = basic_sum + voltage_data(basic_i);
            end
            basic = basic_sum/200;
            max = voltage_data(1);
            for length_i = 1:length(voltage_data)
                if(voltage_data(length_i)<=max)
                    max = voltage_data(length_i);
                    fuhe1_i = length_i;
                end
            end
            if(ch_i==1)
                fuhe2_i = fuhe1_i;
                max2 = max;
            end
            if(ch_i==2&&voltage_data(fuhe2_i)<=max2*0.1)
                fuhe(voltage_i) = fuhe(voltage_i)+1;
            end
            for length_i = 1:length(time_data)-1
                    if(voltage_data(length_i+1)>=voltage_data(length_i))
                        time_1 = length_i+1;
                    end
                    if(voltage_data(length_i+1)==max)
                        time_2 = length_i+1;
                        break
                    end
                end
            voltage_max(j+1) = max-basic;
            time_xiajiang(j+1) = time_2-time_1;
        end
        [mu,sig,muci,sigmaci] = normfit(voltage_max,0.5);
        str1 = strcat('Voltage Max:voltage = ',num2str(voltage(voltage_i)),' CH',num2str(ch(ch_i)),' mu = ',num2str(mu),' sig = ',num2str(sig),' muci = [',num2str(muci(1)),',',num2str(muci(2)),']',' sigmaci = [',num2str(sigmaci(1)),',',num2str(sigmaci(2)),']');
        str2 = strcat('Voltage Max:voltage = ',num2str(voltage(voltage_i)),' CH',num2str(ch(ch_i)));
        disp(str1);
        figure
        histfit(voltage_max)
        title(str2)
        [mu,sig,muci,sigmaci] = normfit(time_xiajiang,0.5);
        str1 = strcat('Time:voltage = ',num2str(voltage(voltage_i)),' CH',num2str(ch(ch_i)),' mu = ',num2str(mu),' sig = ',num2str(sig),' muci = [',num2str(muci(1)),',',num2str(muci(2)),']',' sigmaci = [',num2str(sigmaci(1)),',',num2str(sigmaci(2)),']');
        str2 = strcat('Time:voltage = ',num2str(voltage(voltage_i)),' CH',num2str(ch(ch_i)));
        disp(str1);
        figure
        histfit(time_xiajiang)
        title(str2)
    end
    fuhe(voltage_i) = fuhe(voltage_i)/1000;
    str = strcat('Fuhelv:voltage = ',num2str(voltage(voltage_i)),' fuhelv = ',num2str(fuhe(voltage_i)));
    disp(str);
end