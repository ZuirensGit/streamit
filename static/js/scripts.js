var mr_firstSectionHeight,
    mr_nav,
    mr_navOuterHeight,
    mr_navScrolled = false,
    mr_navFixed = false,
    mr_outOfSight = false,
    mr_floatingProjectSections,
    mr_scrollTop = 0;

$(document).ready(function() {
    "use strict";

    // Smooth scroll to inner links

    $('.inner-link').each(function(){
        var href = $(this).attr('href');
        if(href.charAt(0) !== "#"){
            $(this).removeClass('inner-link');
        }
    });

	if($('.inner-link').length){
		$('.inner-link').smoothScroll({
			offset: -55,
			speed: 800
		});
    }

    // Update scroll variable for scrolling functions

    addEventListener('scroll', function() {
        mr_scrollTop = window.pageYOffset;
    }, false);

    // Append .background-image-holder <img>'s as CSS backgrounds

    $('.background-image-holder').each(function() {
        var imgSrc = $(this).children('img').attr('src');
        $(this).css('background', 'url("' + imgSrc + '")');
        $(this).children('img').hide();
        $(this).css('background-position', 'initial');
    });

    // Fade in background images

    setTimeout(function() {
        $('.background-image-holder').each(function() {
            $(this).addClass('fadeIn');
        });
    }, 200);

    // Initialize Tooltips

    $('[data-toggle="tooltip"]').tooltip();

    // Icon bulleted lists

    $('ul[data-bullet]').each(function(){
        var bullet = $(this).attr('data-bullet');
        $(this).find('li').prepend('<i class="'+bullet+'"></i>');
    });

    // Progress Bars

    $('.progress-bar').each(function() {
        $(this).css('width', $(this).attr('data-progress') + '%');
    });

    // Navigation

    if (!$('nav').hasClass('fixed') && !$('nav').hasClass('absolute')) {

        // Make nav container height of nav

        $('.nav-container').css('min-height', $('nav').outerHeight(true));

        $(window).resize(function() {
            $('.nav-container').css('min-height', $('nav').outerHeight(true));
        });

        // Compensate the height of parallax element for inline nav

        if ($(window).width() > 768) {
            $('.parallax:nth-of-type(1) .background-image-holder').css('top', -($('nav').outerHeight(true)));
        }

        // Adjust fullscreen elements

        if ($(window).width() > 768) {
            $('section.fullscreen:nth-of-type(1)').css('height', ($(window).height() - $('nav').outerHeight(true)));
        }

    } else {
        $('body').addClass('nav-is-overlay');
    }

    if ($('nav').hasClass('bg-dark')) {
        $('.nav-container').addClass('bg-dark');
    }


    // Fix nav to top while scrolling
    //
    // mr_nav = $('body .nav-container nav:first');
    // mr_navOuterHeight = $('body .nav-container nav:first').outerHeight();
    // window.addEventListener("scroll", updateNav, false);

    // Menu dropdown positioning

    // $('.menu > li > ul').each(function() {
    //     var menu = $(this).offset();
    //     var farRight = menu.left + $(this).outerWidth(true);
    //     if (farRight > $(window).width() && !$(this).hasClass('mega-menu')) {
    //         $(this).addClass('make-right');
    //     } else if (farRight > $(window).width() && $(this).hasClass('mega-menu')) {
    //         var isOnScreen = $(window).width() - menu.left;
    //         var difference = $(this).outerWidth(true) - isOnScreen;
    //         $(this).css('margin-left', -(difference));
    //     }
    // });

    // Mobile Menu

    // $('.mobile-toggle').click(function() {
    //     $('.nav-bar').toggleClass('nav-open');
    //     $(this).toggleClass('active');
    // });
    //
    // $('.menu li').click(function(e) {
    //     if (!e) e = window.event;
    //     e.stopPropagation();
    //     if ($(this).find('ul').length) {
    //         $(this).toggleClass('toggle-sub');
    //     } else {
    //         $(this).parents('.toggle-sub').removeClass('toggle-sub');
    //     }
    // });
    //
    // $('.module.widget-handle').click(function() {
    //     $(this).toggleClass('toggle-widget-handle');
    // });
    //
    // $('.search-widget-handle .search-form input').click(function(e){
    //     if (!e) e = window.event;
    //     e.stopPropagation();
    // });

    // Offscreen Nav

    // if($('.offscreen-toggle').length){
    // 	$('body').addClass('has-offscreen-nav');
    // }
    // else{
    //     $('body').removeClass('has-offscreen-nav');
    // }
    //
    // $('.offscreen-toggle').click(function(){
    // 	$('.main-container').toggleClass('reveal-nav');
    // 	$('nav').toggleClass('reveal-nav');
    // 	$('.offscreen-container').toggleClass('reveal-nav');
    // });
    //
    // $('.main-container').click(function(){
    // 	if($(this).hasClass('reveal-nav')){
    // 		$(this).removeClass('reveal-nav');
    // 		$('.offscreen-container').removeClass('reveal-nav');
    // 		$('nav').removeClass('reveal-nav');
    // 	}
    // });
    //
    // $('.offscreen-container a').click(function(){
    // 	$('.offscreen-container').removeClass('reveal-nav');
    // 	$('.main-container').removeClass('reveal-nav');
    // 	$('nav').removeClass('reveal-nav');
    // });


    // Instagram Feed

    if($('.instafeed').length){
    	jQuery.fn.spectragram.accessData = {
			accessToken: '4320925417.c23cd04.311de3c36366422eaa06fe8ca938b9fe',
			clientID: 'c23cd04746df4584a931985119a95b7c'
		};

        $('.instafeed').each(function() {
            var feedID = $(this).attr('data-user-name') + '_';
            $(this).children('ul').spectragram('getUserFeed', {
                query: feedID,
                max: 3
            });
        });
    }



    // Image Sliders

    $('.slider-all-controls').flexslider({
      slideshow: false,
      animationLoop: false,
        start: function(slider){
            if(slider.find('.slides li:first-child').find('.fs-vid-background video').length){
               slider.find('.slides li:first-child').find('.fs-vid-background video').get(0).play();
            }
        },
        after: function(slider){
            if(slider.find('.fs-vid-background video').length){
                if(slider.find('li:not(.flex-active-slide)').find('.fs-vid-background video').length){
                    slider.find('li:not(.flex-active-slide)').find('.fs-vid-background video').get(0).pause();
                }
                if(slider.find('.flex-active-slide').find('.fs-vid-background video').length){
                    slider.find('.flex-active-slide').find('.fs-vid-background video').get(0).play();
                }
            }
        }
    });
    $('.slider-paging-controls').flexslider({
        animation: "slide",
        directionNav: false
    });
    $('.slider-arrow-controls').flexslider({
        controlNav: false
    });
    $('.slider-thumb-controls .slides li').each(function() {
        var imgSrc = $(this).find('img').attr('src');
        $(this).attr('data-thumb', imgSrc);
    });
    $('.slider-thumb-controls').flexslider({
        animation: "slide",
        controlNav: "thumbnails",
        directionNav: true
    });
    $('.logo-carousel').flexslider({
        minItems: 1,
        maxItems: 4,
        move: 1,
        itemWidth: 200,
        itemMargin: 0,
        animation: "slide",
        slideshow: true,
        slideshowSpeed: 3000,
        directionNav: false,
        controlNav: false
    });


    // Multipurpose Modals

    jQuery('.foundry_modal[modal-link]').remove();

    if($('.foundry_modal').length && (!jQuery('.modal-screen').length)){
        // Add a div.modal-screen if there isn't already one there.
        var modalScreen = jQuery('<div />').addClass('modal-screen').appendTo('body');

    }

    jQuery('.foundry_modal').click(function(){
        jQuery(this).addClass('modal-acknowledged');
    });

    $('.modal-container:not([modal-link])').each(function(index) {
        if(jQuery(this).find('iframe[src]').length){
        	jQuery(this).find('.foundry_modal').addClass('iframe-modal');
        	var iframe = jQuery(this).find('iframe');
        	iframe.attr('data-src',iframe.attr('src'));
            iframe.attr('src', '');

        }
        jQuery(this).find('.btn-modal').attr('modal-link', index);

        // Only clone and append to body if there isn't already one there
        if(!jQuery('.foundry_modal[modal-link="'+index+'"]').length){
            jQuery(this).find('.foundry_modal').clone().appendTo('body').attr('modal-link', index).prepend(jQuery('<i class="ti-close close-modal">'));
        }
    });

    $('.btn-modal').unbind('click').click(function(){
    	var linkedModal = jQuery('.foundry_modal[modal-link="' + jQuery(this).attr('modal-link') + '"]');
        jQuery('.modal-screen').toggleClass('reveal-modal');
        if(linkedModal.find('iframe').length){
            if(linkedModal.find('iframe').attr('data-autoplay') === '1'){
                var autoplayMsg = '&autoplay=1'
            }
        	linkedModal.find('iframe').attr('src', (linkedModal.find('iframe').attr('data-src') + autoplayMsg));
        }
        linkedModal.toggleClass('reveal-modal');
        return false;
    });

    // Autoshow modals

	$('.foundry_modal[data-time-delay]').each(function(){
		var modal = $(this);
		var delay = modal.attr('data-time-delay');
		modal.prepend($('<i class="ti-close close-modal">'));
    	if(typeof modal.attr('data-cookie') != "undefined"){
        	if(!mr_cookies.hasItem(modal.attr('data-cookie'))){
                setTimeout(function(){
        			modal.addClass('reveal-modal');
        			$('.modal-screen').addClass('reveal-modal');
        		},delay);
            }
        }else{
            setTimeout(function(){
                modal.addClass('reveal-modal');
                $('.modal-screen').addClass('reveal-modal');
            },delay);
        }
	});

    // Autoclose modals

    $('.foundry_modal[data-hide-after]').each(function(){
        var modal = $(this);
        var delay = modal.attr('data-hide-after');
        if(typeof modal.attr('data-cookie') != "undefined"){
            if(!mr_cookies.hasItem(modal.attr('data-cookie'))){
                setTimeout(function(){
                if(!modal.hasClass('modal-acknowledged')){
                    modal.removeClass('reveal-modal');
                    $('.modal-screen').removeClass('reveal-modal');
                }
                },delay);
            }
        }else{
            setTimeout(function(){
                if(!modal.hasClass('modal-acknowledged')){
                    modal.removeClass('reveal-modal');
                    $('.modal-screen').removeClass('reveal-modal');
                }
            },delay);
        }
    });

    jQuery('.close-modal:not(.modal-strip .close-modal)').unbind('click').click(function(){
    	var modal = jQuery(this).closest('.foundry_modal');
        modal.toggleClass('reveal-modal');
        if(typeof modal.attr('data-cookie') !== "undefined"){
            mr_cookies.setItem(modal.attr('data-cookie'), "true", Infinity);
        }
    	if(modal.find('iframe').length){
            modal.find('iframe').attr('src', '');
        }
        jQuery('.modal-screen').removeClass('reveal-modal');
    });

    jQuery('.modal-screen').unbind('click').click(function(){
        if(jQuery('.foundry_modal.reveal-modal').find('iframe').length){
            jQuery('.foundry_modal.reveal-modal').find('iframe').attr('src', '');
        }
    	jQuery('.foundry_modal.reveal-modal').toggleClass('reveal-modal');
    	jQuery(this).toggleClass('reveal-modal');
    });

    jQuery(document).keyup(function(e) {
		 if (e.keyCode == 27) { // escape key maps to keycode `27`
            if(jQuery('.foundry_modal').find('iframe').length){
                jQuery('.foundry_modal').find('iframe').attr('src', '');
            }
			jQuery('.foundry_modal').removeClass('reveal-modal');
			jQuery('.modal-screen').removeClass('reveal-modal');
		}
	});

    // Modal Strips

    jQuery('.modal-strip').each(function(){
    	if(!jQuery(this).find('.close-modal').length){
    		jQuery(this).append(jQuery('<i class="ti-close close-modal">'));
    	}
    	var modal = jQuery(this);

        if(typeof modal.attr('data-cookie') != "undefined"){

            if(!mr_cookies.hasItem(modal.attr('data-cookie'))){
            	setTimeout(function(){
            		modal.addClass('reveal-modal');
            	},1000);
            }
        }else{
            setTimeout(function(){
                    modal.addClass('reveal-modal');
            },1000);
        }
    });

    jQuery('.modal-strip .close-modal').click(function(){
        var modal = jQuery(this).closest('.modal-strip');
        if(typeof modal.attr('data-cookie') != "undefined"){
            mr_cookies.setItem(modal.attr('data-cookie'), "true", Infinity);
        }
    	jQuery(this).closest('.modal-strip').removeClass('reveal-modal');
    	return false;
    });


    // Video Modals

    jQuery('.close-iframe').click(function() {
        jQuery(this).closest('.modal-video').removeClass('reveal-modal');
        jQuery(this).siblings('iframe').attr('src', '');
        jQuery(this).siblings('video').get(0).pause();
    });

    // Checkboxes

    $('.checkbox-option').on("click",function() {
        $(this).toggleClass('checked');
        var checkbox = $(this).find('input');
        if (checkbox.prop('checked') === false) {
            checkbox.prop('checked', true);
        } else {
            checkbox.prop('checked', false);
        }
    });

    // Radio Buttons

    $('.radio-option').click(function() {

        var checked = $(this).hasClass('checked'); // Get the current status of the radio

        var name = $(this).find('input').attr('name'); // Get the name of the input clicked

        if (!checked) {

            $('input[name="'+name+'"]').parent().removeClass('checked');

            $(this).addClass('checked');

            $(this).find('input').prop('checked', true);

        }

    });


    // Accordions

    $('.accordion li').click(function() {
        if ($(this).closest('.accordion').hasClass('one-open')) {
            $(this).closest('.accordion').find('li').removeClass('active');
            $(this).addClass('active');
        } else {
            $(this).toggleClass('active');
        }
    });

    // Tabbed Content

    $('.tabbed-content').each(function() {
        $(this).append('<ul class="content"></ul>');
    });

    $('.tabs li').each(function() {
        var originalTab = $(this),
            activeClass = "";
        if (originalTab.is('.tabs>li:first-child')) {
            activeClass = ' class="active"';
        }
        var tabContent = originalTab.find('.tab-content').detach().wrap('<li' + activeClass + '></li>').parent();
        originalTab.closest('.tabbed-content').find('.content').append(tabContent);
    });

    $('.tabs li').click(function() {
        $(this).closest('.tabs').find('li').removeClass('active');
        $(this).addClass('active');
        var liIndex = $(this).index() + 1;
        $(this).closest('.tabbed-content').find('.content>li').removeClass('active');
        $(this).closest('.tabbed-content').find('.content>li:nth-of-type(' + liIndex + ')').addClass('active');
    });

});

// function updateNav() {
//
//     var scrollY = mr_scrollTop;
//
//     if (scrollY <= 0) {
//         if (mr_navFixed) {
//             mr_navFixed = false;
//             mr_nav.removeClass('fixed');
//         }
//         if (mr_outOfSight) {
//             mr_outOfSight = false;
//             mr_nav.removeClass('outOfSight');
//         }
//         if (mr_navScrolled) {
//             mr_navScrolled = false;
//             mr_nav.removeClass('scrolled');
//         }
//         return;
//     }
//
//     if (scrollY > mr_firstSectionHeight) {
//         if (!mr_navScrolled) {
//             mr_nav.addClass('scrolled');
//             mr_navScrolled = true;
//             return;
//         }
//     } else {
//         if (scrollY > mr_navOuterHeight) {
//             if (!mr_navFixed) {
//                 mr_nav.addClass('fixed');
//                 mr_navFixed = true;
//             }
//
//             if (scrollY > mr_navOuterHeight * 2) {
//                 if (!mr_outOfSight) {
//                     mr_nav.addClass('outOfSight');
//                     mr_outOfSight = true;
//                 }
//             } else {
//                 if (mr_outOfSight) {
//                     mr_outOfSight = false;
//                     mr_nav.removeClass('outOfSight');
//                 }
//             }
//         } else {
//             if (mr_navFixed) {
//                 mr_navFixed = false;
//                 mr_nav.removeClass('fixed');
//             }
//             if (mr_outOfSight) {
//                 mr_outOfSight = false;
//                 mr_nav.removeClass('outOfSight');
//             }
//         }
//
//         if (mr_navScrolled) {
//             mr_navScrolled = false;
//             mr_nav.removeClass('scrolled');
//         }
//
//     }
// }



// Prepare Signup Form - It is used to retrieve form details from an iframe Mail Chimp or Campaign Monitor form.

function prepareSignup(iFrame){
    var form   = jQuery('<form />'),
        action = iFrame.contents().find('form').attr('action');

    // Alter action for a Mail Chimp-compatible ajax request url.
    if(/list-manage\.com/.test(action)){
       action = action.replace('/post?', '/post-json?') + "&c=?";
       if(action.substr(0,2) == "//"){
           action = 'http:' + action;
       }
    }

    // Alter action for a Campaign Monitor-compatible ajax request url.
    if(/createsend\.com/.test(action)){
       action = action + '?callback=?';
    }


    // Set action on the form
    form.attr('action', action);

    // Clone form input fields from
    iFrame.contents().find('input, select, textarea').not('input[type="submit"]').each(function(){
        $(this).clone().appendTo(form);

    });

    return form;


}



// portrait/landscape changes 100vh

var $mobile = $('.fullscreen'),
portrait = window.innerHeight;
$mobile.css('height', portrait);

// (orientationchange)
window.onorientationchange = function(){
 location.reload();
}
// if(window.innerWidth > window.innerHeight){
//
// // WORKAROUND: converting 90vh to px
// $element = $('.fullscreen');
// function fixMobileSafariViewport() {
// $element.css('height', window.innerHeight * 0.9);
// }
//
// // listen to portrait/landscape changes
// window.addEventListener('orientationchange', fixMobileSafariViewport, true);
// fixMobileSafariViewport();
// }

/*\
|*|  COOKIE LIBRARY THANKS TO MDN
|*|
|*|  A complete cookies reader/writer framework with full unicode support.
|*|
|*|  Revision #1 - September 4, 2014
|*|
|*|  https://developer.mozilla.org/en-US/docs/Web/API/document.cookie
|*|  https://developer.mozilla.org/User:fusionchess
|*|
|*|  This framework is released under the GNU Public License, version 3 or later.
|*|  http://www.gnu.org/licenses/gpl-3.0-standalone.html
|*|
|*|  Syntaxes:
|*|
|*|  * mr_cookies.setItem(name, value[, end[, path[, domain[, secure]]]])
|*|  * mr_cookies.getItem(name)
|*|  * mr_cookies.removeItem(name[, path[, domain]])
|*|  * mr_cookies.hasItem(name)
|*|  * mr_cookies.keys()
|*|
\*/

var mr_cookies = {
  getItem: function (sKey) {
    if (!sKey) { return null; }
    return decodeURIComponent(document.cookie.replace(new RegExp("(?:(?:^|.*;)\\s*" + encodeURIComponent(sKey).replace(/[\-\.\+\*]/g, "\\$&") + "\\s*\\=\\s*([^;]*).*$)|^.*$"), "$1")) || null;
  },
  setItem: function (sKey, sValue, vEnd, sPath, sDomain, bSecure) {
    if (!sKey || /^(?:expires|max\-age|path|domain|secure)$/i.test(sKey)) { return false; }
    var sExpires = "";
    if (vEnd) {
      switch (vEnd.constructor) {
        case Number:
          sExpires = vEnd === Infinity ? "; expires=Fri, 31 Dec 9999 23:59:59 GMT" : "; max-age=" + vEnd;
          break;
        case String:
          sExpires = "; expires=" + vEnd;
          break;
        case Date:
          sExpires = "; expires=" + vEnd.toUTCString();
          break;
      }
    }
    document.cookie = encodeURIComponent(sKey) + "=" + encodeURIComponent(sValue) + sExpires + (sDomain ? "; domain=" + sDomain : "") + (sPath ? "; path=" + sPath : "") + (bSecure ? "; secure" : "");
    return true;
  },
  removeItem: function (sKey, sPath, sDomain) {
    if (!this.hasItem(sKey)) { return false; }
    document.cookie = encodeURIComponent(sKey) + "=; expires=Thu, 01 Jan 1970 00:00:00 GMT" + (sDomain ? "; domain=" + sDomain : "") + (sPath ? "; path=" + sPath : "");
    return true;
  },
  hasItem: function (sKey) {
    if (!sKey) { return false; }
    return (new RegExp("(?:^|;\\s*)" + encodeURIComponent(sKey).replace(/[\-\.\+\*]/g, "\\$&") + "\\s*\\=")).test(document.cookie);
  },
  keys: function () {
    var aKeys = document.cookie.replace(/((?:^|\s*;)[^\=]+)(?=;|$)|^\s*|\s*(?:\=[^;]*)?(?:\1|$)/g, "").split(/\s*(?:\=[^;]*)?;\s*/);
    for (var nLen = aKeys.length, nIdx = 0; nIdx < nLen; nIdx++) { aKeys[nIdx] = decodeURIComponent(aKeys[nIdx]); }
    return aKeys;
  }
};

/*\
|*|  END COOKIE LIBRARY
\*/
