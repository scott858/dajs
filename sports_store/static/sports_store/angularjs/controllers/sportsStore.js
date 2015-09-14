angular.module("sportsStore")
    .constant("dataUrl", "http://localhost:8000/api/v1/sports-store")
    .controller("sportsStoreController", function ($scope, $http, dataUrl) {
        $scope.data = {};
        $http.get(dataUrl)
            .success(function (data) {
                $scope.data.products = data;
            })
            .error(function (error) {
                $scope.data.error = error;
            })
    });