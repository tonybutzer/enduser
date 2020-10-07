from time import time
import xarray as xr

def _get_year_month(product, tif):
    fn = tif.split('/')[-1]
    fn = fn.replace(product,'')
    fn = fn.replace('.tif','')
    print(fn)
    return fn


def xr_build_cube_concat_ds(tif_list, product):

    start = time()
    my_da_list =[]
    year_month_list = []
    for tif in tif_list:
        #tiffile = 's3://dev-et-data/' + tif
        tiffile = tif
        print(tiffile)
        da = xr.open_rasterio(tiffile)
        #da = da.squeeze().drop(labels='band')
        #da.name=product
        my_da_list.append(da)
        tnow = time()
        elapsed = tnow - start
        print(tif, elapsed)
        year_month_list.append(_get_year_month(product, tif))

    da = xr.concat(my_da_list, dim='band')
    da = da.rename({'band':'year_month'})
    da = da.assign_coords(year_month=year_month_list)
    DS = da.to_dataset(name=product)
    return(DS)
