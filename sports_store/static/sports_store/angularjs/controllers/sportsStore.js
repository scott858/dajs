angular.module("sportsStore")
    .constant("dataUrl", "/api/v1/products")
    .constant("orderUrl", "/api/v1/orders")
    .controller("sportsStoreController", function ($scope, $http, $location, dataUrl, orderUrl, cart) {

        $scope.data = {};

        $http.get(dataUrl)
            .success(function (data) {
                $scope.data.products = data;
            })
            .error(function (error) {
                $scope.data.error = error;
            });

        $scope.sendOrder = function (shippingDetails) {
            var order = angular.copy(shippingDetails);
            order.products = cart.getProducts();
            $http.post(orderUrl, order)
                .success(function (data) {
                    $scope.data.orderId = data.id;
                    cart.getProducts().length = 0;
                })
                .error(function (error) {
                    $scope.data.orderError = error;
                })
                .finally(function () {
                    $location.path("/complete")
                });
        }
    });