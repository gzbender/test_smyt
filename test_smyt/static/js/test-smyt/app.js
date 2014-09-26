var testSmyt = angular.module('testSmyt', ['ngRoute', 'testSmytControllers']);

testSmyt.config(['$routeProvider', function($routeProvider) {
    $routeProvider
      .when('/object-list/:model', {controller: 'ObjectListCtrl',
            templateUrl: window.STATIC_URL + 'js/test-smyt/object-list.html'});
  }]);