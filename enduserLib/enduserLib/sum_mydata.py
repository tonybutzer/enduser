import datetime
import os
import time
import rasterio
import numpy as np
#read in file with rasterio
def _read_file(file):
    print("reading file ...", file)
    with rasterio.open(file) as src:
        return(src.read(1))

def monthly_sum(file_list, out_dir, out_product, year):
# what months to summarize
    start_mon = 1 #start month
    end_mon = 12 #end month


    #loop through month 1,2,..12    
    for i in range(start_mon,(end_mon+1)): 
        print('Month summed up is: ' + str(i))
        Listras = [] 
        for et_in in file_list:
            doy = int(et_in.split('.')[0][-3:])
            #doy = int(et_in[-3:])
            #print 'Day of the year: ' + str(doy)
            datea = str(datetime.date(year,1,1) + datetime.timedelta(doy-1))
            mon = int(datea.split('-')[1])
            #print 'Month is: ' + str(mon)
            if mon == i: #if month = i then append grid to list for summing up
                Listras.append(et_in)
        #print('daily grids for month ' + str(i) + ' :')
        #print(Listras)
        if Listras == []:
            print('No daily data for month' + str(i) + ' available..continue to next month')
            continue
        else:
            # Read all data as a list of numpy arrays 
            array_list = [_read_file(x) for x in Listras]
            
            array_out = np.sum(array_list, axis=0)

            # Get metadata from one of the input files
            with rasterio.open(file_list[0]) as src:
                meta = src.meta
            meta.update(dtype=rasterio.float32)

            # Write output file
            #out_name = 'ppt_avg_' + str(year) + (('0'+ str(i))[-2:]) +'.tif'
            out_name = out_product + str(year) + (('0'+ str(i))[-2:]) +'.tif'

            with rasterio.open(out_dir + '/' + out_name, 'w', **meta) as dst:
                dst.write(array_out.astype(rasterio.float32), 1)

            print('Created monthly grid!', out_name)
