import import_api
import export_api
import ApiTypes

def import_garment_image(image_path):
    option = ApiTypes.ImportExportOption()
    option.bImportGarment = True
    return import_api.ImportFile(image_path, option)

def export_garment_usd(output_path):
    option = ApiTypes.ImportExportOption()
    option.bExportGarment = True
    option.bSingleObject = True
    return export_api.ExportUSD(output_path, option)
