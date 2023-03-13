function createCountUp() {
  var elements = [].slice.call(document.querySelectorAll('[data-kt-countup="true"]:not(.counted)'));

  elements.map(function (element) {
    if (element.getAttribute("data-kt-initialized") === "1") {
      return;
    }

    var options = {};

    var value = element.getAttribute('data-kt-countup-value');
    value = parseFloat(value.replace(/,/g, ""));

    if (element.hasAttribute('data-kt-countup-start-val')) {
      options.startVal = parseFloat(element.getAttribute('data-kt-countup-start-val'));
    }

    if (element.hasAttribute('data-kt-countup-duration')) {
      options.duration = parseInt(element.getAttribute('data-kt-countup-duration'));
    }

    if (element.hasAttribute('data-kt-countup-decimal-places')) {
      options.decimalPlaces = parseInt(element.getAttribute('data-kt-countup-decimal-places'));
    }

    if (element.hasAttribute('data-kt-countup-prefix')) {
      options.prefix = element.getAttribute('data-kt-countup-prefix');
    }

    if (element.hasAttribute('data-kt-countup-separator')) {
      options.separator = element.getAttribute('data-kt-countup-separator');
    }

    if (element.hasAttribute('data-kt-countup-suffix')) {
      options.suffix = element.getAttribute('data-kt-countup-suffix');
    }

    var count = new countUp.CountUp(element, value, options);

    count.start();

    element.classList.add('counted');

    element.setAttribute("data-kt-initialized", "1");
  });
}