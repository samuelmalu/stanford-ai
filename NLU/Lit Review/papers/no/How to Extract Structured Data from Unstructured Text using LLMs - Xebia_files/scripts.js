'use strict';
/*
This script must be loaded as type="module" (see functions.php).
Modules are automagically loaded asynchronously
and executed in source order when the DOM is ready.
Works in all modern browsers (i.e. not Internet Explorer 11).
*/

//#region jQuery

const NAV_ANIMATION = 200;

function toggle_desktop_menu(event_object) {
    jQuery(this).toggleClass('is-open');
    event_object.preventDefault();
}

jQuery('.has-menu').click(toggle_desktop_menu);

function toggle_mobile_menu(e) {
    jQuery('body').toggleClass('nav-open');
    e.preventDefault();
}

jQuery('.btn-nav').on('click', toggle_mobile_menu);

function toggle_mobile_navigation_dropdown() {
    const $this = jQuery(this);

    if ($this.hasClass('is-open')) {
        $this.removeClass('is-open').find('.sub-menu').slideUp(NAV_ANIMATION);
    } else {
        $this.addClass('is-open').find('.sub-menu').slideDown(NAV_ANIMATION);
    }
}

jQuery('.nav-mobile .menu-item-has-children').click(
    toggle_mobile_navigation_dropdown
);

const EXPANDED = 'aria-expanded';

function toggle_targets() {
    const $this = jQuery(this);

    if ($this.attr(EXPANDED) === 'true') {
        $this
            .attr(EXPANDED, 'false')
            .closest('.toggle-box')
            .find('.toggle-target')
            .slideUp(NAV_ANIMATION);
    } else {
        $this
            .attr(EXPANDED, 'true')
            .closest('.toggle-box')
            .find('.toggle-target')
            .slideDown(NAV_ANIMATION);
    }
}

jQuery(`.toggle-title [${EXPANDED}]`).click(toggle_targets);

//#endregion

//#region A11y: motion

const MOTION = 'reduced-motion';
const STYLE = `
<style>
:host { display: none }
@media (prefers-${MOTION}) {
  :host { --${MOTION}: 1 }
}
</style>
`;

customElements.define(
    'a11y-user',
    class extends HTMLElement {
        constructor() {
            super();
            this.attachShadow({ mode: 'open' }).innerHTML = STYLE;
        }
    }
);

const probe = document.createElement('a11y-user');

const getCustomProperty = key =>
    getComputedStyle(probe).getPropertyValue(`--${key}`);

document.body.appendChild(probe);

const reduce_motion = Boolean(Number(getCustomProperty(MOTION)));

document.body.removeChild(probe);

//#endregion

//#region Scroll to Focus
/*
Scroll the focused element to the middle of the screen
(its position in and the height of the page permitting).
Note that activating interactive elements also sets focus,
so we use mousedown and touchstart to opt out early.
The order of relevant events is:
- mousedown / touchstart
- focusin (NB: the focus event does not bubble)
- click (triggered by mouse click, enter key and touch tap)
*/

const link_selector = 'a[href]';
const tab_selector = [
    link_selector,
    'button',
    'input',
    'select',
    'textarea',
].join();

const is_tabbable = element => element.matches(tab_selector);

const behavior = reduce_motion ? 'auto' : 'smooth';

function scroll_into_view(element, block = 'center') {
    element.scrollIntoView({
        behavior,
        block,
    });
}

let click_target = null;

function on_focus({ target }) {
    if (!is_tabbable(target)) {
        return;
    }

    if (target === click_target) {
        click_target = null;
    } else {
        scroll_into_view(target);
    }
}

const get_link = node => node.closest(link_selector);

const get_tabbable = node => node.closest(tab_selector);

function on_pointer({ target }) {
    click_target = get_tabbable(target);
}

document.addEventListener('focusin', on_focus);
document.addEventListener('mousedown', on_pointer);
document.addEventListener('touchstart', on_pointer);

//#endregion

{
    // /* Smooth Scroll widget
    function scroll_to_fragment(id) {
        const destination = document.getElementById(id);

        scroll_into_view(destination, 'start');
        history.pushState(null, null, `#${id}`);

        // NB: don't use the tabIndex *property* here
        if (!destination.getAttribute('tabindex')) {
            destination.setAttribute('tabindex', '-1');
        }

        destination.focus({
            preventScroll: true,
        });
    }

    function on_click(click_event) {
        const { target } = click_event;
        const link = get_link(target);

        if (link) {
            const [, hash] = link.href.split('#');

            if (hash && !hash.startsWith('=')) {
                scroll_to_fragment(hash);
                click_event.preventDefault();
            }
        }
    }
    document.addEventListener('click', on_click);
}

// Sticky nav
window.onscroll = function () {
    scrollNav();
};

function scrollNav() {
    const siteHeaderNavEl = document.querySelector('.site-header-nav');
    if (
        document.body.scrollTop > 50 ||
        document.documentElement.scrollTop > 50
    ) {
        siteHeaderNavEl?.classList.add('is-gone');
    } else {
        siteHeaderNavEl?.classList.remove('is-gone');
    }
}

// SLIDERS
// Sliders
var $casesSlider = jQuery('.cases-slider-main').flickity({
    pageDots: false,
    initialIndex: 1,
    bgLazyLoad: 2,
    fade: true,
    wrapAround: true,
    prevNextButtons: false,
});

var $casesLogosSlider = jQuery('.cases-slider-nav').flickity({
    asNavFor: '.cases-slider-main',
    contain: true,
    pageDots: false,
    prevNextButtons: false,
    imagesLoaded: true,
    initialIndex: 1,
});

jQuery('.cases-slider-wrap .btn-left').on('click', function () {
    $casesSlider.flickity('previous');
});
jQuery('.cases-slider-wrap .btn-right').on('click', function () {
    $casesSlider.flickity('next');
});

// var $casesSmSlider = jQuery('.slider-cases-sm').flickity({
//     pageDots: false,
//     wrapAround: false,
//     initialIndex: 0,
//     prevNextButtons: false,
//     bgLazyLoad: 3,
//     cellAlign: 'left'
// });

// jQuery('.cases-sm-nav .btn-left').on('click', function() {
//     $casesSmSlider.flickity('previous');
// });
// jQuery('.cases-sm-nav .btn-right').on('click', function() {
//     $casesSmSlider.flickity('next');
// });

//Remove wave bg if there is a CTA on the page
if (jQuery('.footer-cta').length > 0) {
    jQuery('body').removeClass('body-wave');
}

//Team Slider
jQuery('.team-slider-wrap').each(function () {
    var $teamSlider = jQuery(this).find('.team-slider').flickity({
        pageDots: false,
        prevNextButtons: false,
        cellSelector: '.team-slider-box',
        imagesLoaded: true,
        groupCells: 1,
        cellAlign: 'left',
        selectedAttraction: 0.01,
        friction: 0.15,
    });
    var prevBtn = jQuery(this).find('.btn-left');
    var nextBtn = jQuery(this).find('.btn-right');
    jQuery(prevBtn).on('click', function () {
        $teamSlider.flickity('previous');
    });
    jQuery(nextBtn).on('click', function () {
        $teamSlider.flickity('next');
    });
});

//Logos Slider
jQuery('.logo-slider-wrap').each(function () {
    var $logosLider = jQuery(this).find('.logo-slider').flickity({
        contain: true,
        pageDots: false,
        prevNextButtons: false,
        imagesLoaded: true,
        cellAlign: 'left',
        draggable: false,
        wrapAround: true,
        setGallerySize: true,
        initialIndex: 1,
    });
    var prevBtn = jQuery(this).find('.btn-left');
    var nextBtn = jQuery(this).find('.btn-right');
    jQuery(prevBtn).on('click', function () {
        $logosLider.flickity('previous');
    });
    jQuery(nextBtn).on('click', function () {
        $logosLider.flickity('next');
    });
});

//Staggered delays
function addDelay(delayTarget, motionType, delayCounter, delayAmount) {
    jQuery(delayTarget).each(function () {
        jQuery(this)
            .children()
            .each(function () {
                delayCounter += delayAmount;
                jQuery(this).css(motionType + '-delay', delayCounter + 's');
            });
    });
}
// addDelay('.data-appear-group', 'transition', -0.20, 0.20);
addDelay('.data-appear-group-sm', 'transition', 0.2, 0.1);
addDelay('.h-delay', 'transition', 0.4, 0.1);

//Staggered delays
function addDelayOld(delayTarget, delayAmount) {
    jQuery(delayTarget).each(function () {
        var delayCounter = -0.15;
        jQuery(this)
            .children()
            .each(function () {
                delayCounter += delayAmount;
                jQuery(this).css('transition-delay', delayCounter + 's');
            });
    });
}
addDelayOld('.data-appear-group', 0.15);

//Toggle tabs
if (jQuery('.tabs-wrap')) {
    jQuery('.tab-content-wrap .tab-content:first-child').addClass('is-active');
    jQuery('.tabs-wrap .tab-title:first-child').addClass('is-active');
}

jQuery('.tab-title').click(function () {
    jQuery('.tab-title').removeClass('is-active');
    jQuery('.tab-content').removeClass('is-active');
    var currentId = jQuery(this).attr('id');
    var contentID = 's-' + currentId;

    var thisIndex = jQuery(this).index() + 1;

    jQuery(this).addClass('is-active');
    jQuery('#' + contentID).addClass('is-active');
});

document.querySelectorAll('.wpcf7-form')?.forEach(formEl => {
    const msgEl = formEl.querySelector('.wpcf7-response-output');

    const observer = new MutationObserver(mutations => {
        msgEl?.scrollIntoView({ behavior: "smooth", block: "center" });
    });

    observer.observe(formEl, {
        attributes: true,
        attributeFilter: ['class'],
        childList: false,
        characterData: false
    });
});
