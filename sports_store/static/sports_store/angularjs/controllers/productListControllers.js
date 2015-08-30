angular.module("sportsStore")
    .constant("productListActiveClass", "btn-primary")
    .controller("productListController", function ($scope, $filter, productListActiveClass) {
        var selectedCategory = null;

        $scope.selectCategory = function (newCategory) {
            selectedCategory = newCategory;
        };

        $scope.categoryFilterFn = function (product) {
            return selectedCategory == null || product.category == selectedCategory;
        };

        $scope.getCategoryClass = function (category) {
            return selectedCategory == category ? productListActiveClass : "";
        };
    }
);