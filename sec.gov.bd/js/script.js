jQuery(function ($) {
	'use strict';

	/* ----------------------------------------------------------- */
	/*  Scroll smothly and button hide show
	/* ----------------------------------------------------------- */
	$(window).on('scroll', function () {
		
		// scroll to top btn show/hide
		function scrollTopBtn() {
			var scrollToTop = $('#back-to-top'),
				scroll = $(window).scrollTop();
			if (scroll >= 50) {
				scrollToTop.fadeIn();
			} else {
				scrollToTop.fadeOut();
			}
		}
		scrollTopBtn();
	});

	$(document).ready(function () {

		// back to top
		function backToTop() {
			$('#back-to-top').on('click', function () {
				$('#back-to-top').tooltip('hide');
				$('body,html').animate({
					scrollTop: 0
				}, 800);
				return false;
			});
		}
		backToTop();
	});
});









// Designed By Shaon Talukder Dwip