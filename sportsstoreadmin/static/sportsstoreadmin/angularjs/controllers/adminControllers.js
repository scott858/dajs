angular.module("sportsStoreAdmin")
    .constant("authUrl", "/sports-store-admin/login/")
    .constant("ordersUrl", "/api/v1/orders/")
    .constant("productsUrl", "/api/v1/products/")
    .controller("authController", function ($scope, $http, $location, authUrl) {

        $scope.authenticate = function (user, pass) {
            $http({
                url: authUrl,
                method: "POST",
                data: $.param({username: user, password: pass}),
                config: {withCredentials: true},
                headers: {'Content-Type': 'application/x-www-form-urlencoded; charset-UTF-8'}
            })
                .success(function (data) {
                    $location.path("/main");
                })
                .error(function (error) {
                    $scope.authenticationError = error;
                });
        }
    })
    .controller("mainController", function ($scope) {
        $scope.screens = ["Products", "Orders"];
        $scope.current = $scope.screens[0];

        $scope.setScreen = function (index) {
            $scope.current = $scope.screens[index];
        };

        $scope.getScreen = function () {
            return $scope.current == "Products" ? "products" : "orders";
        };

    })
    .controller("ordersController", function ($scope, $http, ordersUrl) {
        $http.get(ordersUrl, {withCredentials: true})
            .success(function (data) {
                $scope.orders = data;
            })
            .error(function (error) {
                $scope.error = error;
            });

        $scope.selectedOrder = function (order) {
            $scope.selectedOrder = order;
        };

        $scope.calcTotal = function (order) {
            var total = 0;
            for (var i = 0; i < order.products.length; i++) {
                total += order.products[i].count * order.products[i].price;
            }
            return total;
        }
    }
);