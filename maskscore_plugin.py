import import_api
import export_api
import ApiTypes
import random

# Sample a random garment from the dataset
# This is a placeholder for the actual dataset sampling logic
garment_id = "sample_garment_id"
image_path = f"C:/contract-manifest/data/{garment_id}.png"

# Import image into Marvelous Designer
option = ApiTypes.ImportExportOption()
option.bImportGarment = True

# Import file
import_api.ImportFile(image_path, option)

# Export as OpenUSD
export_option = ApiTypes.ImportExportOption()
export_option.bExportGarment = True
export_option.bSingleObject = True

export_api.ExportUSD(f"C:/contract-manifest/output/{garment_id}.usda", export_option)
