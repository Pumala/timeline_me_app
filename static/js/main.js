var app = angular.module('timeline_Me_App', ['ui.router', 'ngCookies']);

app.factory('TimelineFactory', function($http, $cookies, $rootScope) {
  var service = {};

  return service;
});

app.config(function($stateProvider, $urlRouterProvider) {
  $stateProvider
  .state({
    name: 'home',
    url: '/',
    templateUrl: 'home.html',
    controller: 'HomeController'
  })
  .state({
    name: 'signup',
    url: '/signup',
    templateUrl: 'signup.html',
    controller: 'SignUpController'
  })
  .state({
    name: 'login',
    url: '/login',
    templateUrl: 'login.html',
    controller: 'LoginController'
  })

  $urlRouterProvider.otherwise('/');

});

app.controller('HomeController', function($rootScope) {

});

app.controller('SignUpController', function($rootScope) {

});

app.controller('LoginController', function($rootScope) {

});
