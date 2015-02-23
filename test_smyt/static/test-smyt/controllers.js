var testSmytControllers = angular.module('testSmytControllers', []);

testSmytControllers.controller('ObjectListCtrl', ['$scope', '$route', 'ObjectsResource',
    function($scope, $route, ObjectsResource){
        'use strict';
        function updateList(){
            ObjectsResource.query({model: $scope.model}, function(data){
                var objects = [];
                for(var i=0; i<data.objects.length; i++){
                    objects.push(new ObjectsResource(data.objects[i]));
                }
                $scope.objects = objects;
                $scope.fields = data.fields;
            });
        }
        $scope.model = $route.current.params.model;
        $scope.objects = [];
        $scope.fields = [];
        $scope.newObj = new ObjectsResource;
        $scope.create = function(){
            $scope.newObj.$create({model: $scope.model}, function(data){
                $scope.newObj = new ObjectsResource;
                updateList();
            });
        }
        updateList();
}]);