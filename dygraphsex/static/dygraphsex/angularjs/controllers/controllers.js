var controllersModule = angular.module("exampleApp.Controllers", []);

controllersModule.controller("dygraphController", function ($scope, days) {
    $scope.plot = new Dygraph(
        document.getElementById("graphdiv2"),
        "/cell_data/ivt_measurement.csv", // path to CSV file
        {}          // options
    );
});

