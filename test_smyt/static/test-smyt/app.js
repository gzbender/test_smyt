var testSmyt = angular.module('testSmyt', ['ngRoute', 'testSmytControllers', 'testSmytDirectives', 'testSmytResources']);

testSmyt.run(function($http){
	var csrf = getCookie('csrftoken');
    $http.defaults.headers.post['X-CSRFToken'] = csrf;
    $http.defaults.headers.patch['X-CSRFToken'] = csrf;
});

testSmyt.config(['$routeProvider', function($routeProvider) {
    $routeProvider
      .when('/object-list/:model', {controller: 'ObjectListCtrl',
            templateUrl: window.STATIC_URL + 'test-smyt/tmpl/object-list.html'});
}]);