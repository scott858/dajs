var controllersModule = angular.module("exampleApp.Controllers", []);

controllersModule.controller("dayController", function ($scope, days) {
    $scope.day = days.today;
});

controllersModule.controller("tomorrowController", function ($scope, days) {
    $scope.day = days.tomorrow;
});

