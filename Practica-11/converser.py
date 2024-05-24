import pandas as pd

namefiles = [
    "./Materiales/IRIS/iris.data",
    "./Materiales/Wine/wine.data",
    "./Materiales/Breast Cancer Wisconsin/wdbc.data",
]

headers = [
    ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"],
    ["class","alcohol", "malic_acid", "ash", "alcalinity_of_ash", "magnesium", "total_phenols", "flavanoids", "nonflavanoid_phenols", "proanthocyanins", "color_intensity", "hue", "OD280/OD315_of_diluted_wines", "proline"],
    ["id", "diagnosis", "radius_mean", "texture_mean", "perimeter_mean", "area_mean", "smoothness_mean", "compactness_mean", "concavity_mean", "concave_points_mean", "symmetry_mean", "fractal_dimension_mean", "radius_se", "texture_se", "perimeter_se", "area_se", "smoothness_se", "compactness_se", "concavity_se", "concave_points_se", "symmetry_se", "fractal_dimension_se", "radius_worst", "texture_worst", "perimeter_worst", "area_worst", "smoothness_worst", "compactness_worst", "concavity_worst", "concave_points_worst", "symmetry_worst", "fractal_dimension_worst"]
]

for namefile in namefiles:
    data = pd.read_csv(namefile, header=None)
    data.columns = headers[namefiles.index(namefile)]
    data.to_csv(namefile+".csv", index=False)

# Del data wine, cambiar class a string
data = pd.read_csv(namefiles[1]+".csv")
data["class"] = data["class"].astype(str) + " class"
data.to_csv(namefiles[1]+".csv", index=False)

print("Conversiones realizadas con exito")