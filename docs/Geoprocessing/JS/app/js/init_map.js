require([
    "esri/Map",
    "esri/views/MapView",
    "esri/layers/FeatureLayer",
    "esri/widgets/Search",
    "esri/widgets/Home",
    "esri/widgets/Legend",
    "esri/core/promiseUtils",
    "esri/layers/GraphicsLayer",
    "esri/Graphic"
], function(Map, MapView, FeatureLayer, Search, Home, Legend, promiseUtils, GraphicsLayer, Graphic) {

    const layer = new FeatureLayer({
        url: "https://services2.arcgis.com/VNo0ht0YPXJoI4oE/arcgis/rest/services/WV_County_Layer/FeatureServer/0",
        outFields: ["*"]
    });

    const selectionLayer = new GraphicsLayer();

    const map = new Map({
        basemap: "topo-vector",
        layers: [layer, selectionLayer]  // Add selectionLayer to the map
    });

    const view = new MapView({
        container: "viewDiv",
        map: map,
        center: [-80.35, 38.75],
        zoom: 8
    });

    const searchWidget = new Search({
        view: view
    });
    view.ui.add(searchWidget, {
        position: "top-left",
        index: 0
    });

    const homeWidget = new Home({
        view: view
    });
    view.ui.add(homeWidget, {
        position: "top-left",
        index: 2
    });

    const legend = new Legend({
        view: view
    });
    view.ui.add(legend, "bottom-left");


    // Add function to show info popup
    function showPopup() {
        document.getElementById("info-popup").classList.add("active");
        document.getElementById("map-container").style.width = "calc(100% - 400px)";
    }

    function hidePopup() {
        document.getElementById("info-popup").classList.remove("active");
        document.getElementById("map-container").style.width = "100%";
    }

    // Variable to keep track of the selected feature and graphic
    let selectedFeature = null;
    let selectedGraphic = null;

    view.when(() => {
        view.on("click", (event) => {
            const opts = {
                include: layer
            };

            view.hitTest(event, opts).then((response) => {
                if (response.results.length) {
                    const graphic = response.results[0].graphic;

                    // Remove previous selection
                    selectionLayer.removeAll();

                    if (selectedFeature && selectedFeature.attributes.OBJECTID === graphic.attributes.OBJECTID) {
                        // Unselect the feature and zoom out
                        selectedFeature = null;
                        document.getElementById("selected-county").style.display = "none";
                        view.goTo({
                            center: [-80.35, 38.75],
                            zoom: 8
                        });
                        hidePopup(); // Hide the popup when unselecting the feature
                    } else {
                        // Select the feature and zoom in
                        selectedFeature = graphic;
                        document.getElementById("selected-county").textContent = selectedFeature.attributes.GSL_NAME + " COUNTY";
                        document.getElementById("selected-county").style.display = "block";
                        view.goTo({
                            target: graphic.geometry,
                            zoom: 10
                        });

                        // Create a new Graphic for the selection indicator
                        selectedGraphic = new Graphic({
                            geometry: graphic.geometry,
                            symbol: {
                                type: "simple-fill",
                                color: [0, 0, 0, 0],
                                outline: {
                                    color: [0, 255, 255, 1],
                                    width: 3
                                }
                            }
                        });

                        // Add the selection indicator to the graphics layer
                        selectionLayer.add(selectedGraphic);
                        showPopup(); // Show the popup when selecting a feature
                    }

                    console.log("Selected Feature:", selectedFeature ? selectedFeature.attributes.GSL_NAME : "None");
                } else {
                    // If no feature was clicked, clear selection and zoom out
                    selectedFeature = null;
                    document.getElementById("selected-county").style.display = "none";
                    selectionLayer.removeAll();
                    view.goTo({
                        center: [-80.35, 38.75],
                        zoom: 8
                    });
                    hidePopup(); // Hide the popup when no feature is clicked
                }
            });
        });
    });

    function capitalizeFirstLetter(string) {
        return string.charAt(0).toUpperCase() + string.slice(1).toLowerCase();
    }

    // Add functionality for report generation
    document.getElementById("create-report").addEventListener("click", function() {
        if (!selectedFeature) {
            // No feature selected, show warning
            const warningElement = document.getElementById("warning-message");
            warningElement.textContent = "Please select a entity before creating a report.";
            warningElement.style.display = "block";

            // Hide the warning after 5 seconds
            setTimeout(() => {
                warningElement.style.display = "none";
            }, 5000);
        } else {
            // Feature selected, open new page with report
            const countyName = capitalizeFirstLetter(selectedFeature.attributes.GSL_NAME);
            const reportUrl = `http://gistc-websrv1-22.wvu-ad.wvu.edu:8080/report/?name=${encodeURIComponent(countyName)}`;
            window.open(reportUrl, '_blank');
        }
    });
    
});
