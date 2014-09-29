var testSmytControllers = angular.module('testSmytControllers', []);

testSmytControllers.controller('ObjectListCtrl', ['$scope', '$routeParams', '$http',
    function($scope, $routeParams, $http){
        var _editing = [],
            maxId = 5,
            model = $routeParams.model;
        $http.get(window.API_URLS.objects.replace(':model', model))
            .success(function(data){
                $scope.objects = data.objects;
                $scope.fields = data.fields;
            });
        $scope.newObj = {};
        $scope.edit = function(objectId, field){
            _editing = [objectId, field];
        }
        $scope.isEdit = function(objectId, field){
            return angular.equals(_editing, [objectId, field]);
        }
        $scope.create = function(){
            $http.post(window.API_URLS.objects.replace(':model', model), $scope.newObj)
                .success(function(data){
                    $scope.newObj = {};
                    $scope.objects.push(data);
                })
        }
}]);