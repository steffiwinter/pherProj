import xarray as xr
import dask

def load_sst_data():
    ds_sst = xr.open_dataset(
        "/home/jovyan/my_materials/data/sst_1m.nc",
        chunks="auto",
    )

    # Variablen und Koordinaten umbenennen
    ds_sst = ds_sst.rename_vars(sea_surface_temperature="sst")
    ds_sst = ds_sst.rename({'latitude': 'lat', 'longitude': 'lon'})

    # Spezifische Variable 'sst' auswählen
    #sst = ds_sst['sst']
        
    # NaN-Punkte identifizieren
    #mask = sst.notnull().any(dim="time").compute()

    # Entferne Punkte mit NaN (Alternative zu drop=True)
    #sst_clean = sst.where(mask)
    #sst_clean = sst_clean.dropna(dim="lat", how="all").dropna(dim="lon", how="all")

    # Transponiere zu konsistenter Dimension
    #sst_clean = sst_clean.transpose("lat", "lon", "time")

    # Bereinigte Daten zurück ins Dataset schreiben
    #ds_sst['sst'] = sst_clean

    return ds_sst