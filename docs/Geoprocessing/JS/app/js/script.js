require([
    "esri/Map",
    "esri/views/MapView",
    "esri/layers/FeatureLayer",
    "esri/layers/GraphicsLayer",
    "esri/widgets/ScaleBar",
    "esri/widgets/Home",
    "esri/widgets/Fullscreen",
    "esri/widgets/LayerList",
    "esri/widgets/Legend",
    "esri/widgets/BasemapGallery",
    "esri/widgets/Search",
    "esri/widgets/Expand",
    "esri/widgets/Sketch"
], function (Map, MapView, FeatureLayer, GraphicsLayer, ScaleBar, Home, Fullscreen, LayerList, Legend, BasemapGallery, Search, Expand, Sketch) {
    var map = new Map({
        basemap: "topo-vector",
    });

    const view = new MapView({
        container: "viewDiv",
        map: map,
        center: [-77.70543, 40.85700],
        zoom: 8
    });

    // Define a pop-up for Trailheads
    const popupTrailheads = {
        "title": "Trailhead",
        "content":
            "<b>Trail:</b> {TRL_NAME}<br>\
            <b>City:</b> {CITY_JUR}<br>\
            <b>Cross Street:</b> {X_STREET}<br>\
            <b>Parking:</b> {PARKING}<br>\
            <b>Elevation:</b> {ELEV_FT} ft<br>\
            <b>Latitude:</b> {LAT}<br>\
            <b>Longitude:</b> {LON}"
    }

    var featureLayer = new FeatureLayer({
        url: "https://services2.arcgis.com/VNo0ht0YPXJoI4oE/arcgis/rest/services/StorageTankLocations_Active2024_05/FeatureServer/0",
        popupTemplate: popupTrailheads
    });

    map.add(featureLayer);

    var graphicsLayer = new GraphicsLayer();
    map.add(graphicsLayer);

    var legend = new Legend({ view: view });
    view.ui.add(legend, "bottom-left");

    view.on("click", function(event) {
        var lat = event.mapPoint.latitude;
        var lon = event.mapPoint.longitude;
        console.log("Latitude: " + lat + ", Longitude: " + lon);
    });

    var basemapGallery = new BasemapGallery({ view: view });
    var bgExpand = new Expand({ view: view, content: basemapGallery });
    view.ui.add(bgExpand, "top-left");

    var scaleBar = new ScaleBar({ view: view, unit: "metric" });
    view.ui.add(scaleBar, "bottom-right");

    var home = new Home({ view: view });
    view.ui.add(home, "top-left");

    var fullscreen = new Fullscreen({ view: view });
    view.ui.add(fullscreen, "top-left");

    var layerList = new LayerList({ view: view });
    view.ui.add(layerList, "top-right");
    
    var search = new Search({ view: view });
    view.ui.add(search, "top-right");
    
    var sketch = new Sketch({
        view: view,
        layer: graphicsLayer,
        creationMode: "update" // Allow only adding points
    });

    view.ui.add(sketch, "top-right");

    // Listen for sketch "create" event
    sketch.on("create", function(event) {
        if (event.state === "complete" && event.graphic.geometry.type === "point") {
            var lat = event.graphic.geometry.latitude;
            var lon = event.graphic.geometry.longitude;
            console.log("Added point - Latitude: " + lat + ", Longitude: " + lon);

            // Try to post to the feature layer
            featureLayer.applyEdits({
                addFeatures: [{
                    geometry: {
                        type: "point",
                        latitude: lat,
                        longitude: lon
                    },
                    attributes: {} // You can add attributes if needed
                }]
            }).then(function(result) {
                console.log("Point added successfully");
            }).catch(function(error) {
                console.error("Error adding point: ", error);
            });
        }
    });
});
