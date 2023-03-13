const KTInitToastr = (function () {
  let alerts;

  function initToastr() {
    toastr.options = {
      "closeButton": false,
      "debug": false,
      "newestOnTop": false,
      "progressBar": false,
      "positionClass": "toastr-bottom-right",
      "preventDuplicates": false,
      "onclick": null,
      "showDuration": "300",
      "hideDuration": "1000",
      "timeOut": "7000",
      "extendedTimeOut": "1000",
      "showEasing": "swing",
      "hideEasing": "linear",
      "showMethod": "fadeIn",
      "hideMethod": "fadeOut"
    };

    alerts.forEach(alert => {
      if (alert.getAttribute('data-toastr-mode') == 'error') {
        toastr.error(alert.innerText);
      } else {
        toastr.success(alert.innerText);
      }
    });
  }

  return {
    init: function () {
      alerts = document.querySelectorAll('[data-toastr="toastr"]');
      initToastr();
    },
  };
})();

KTUtil.onDOMContentLoaded(function () {
  KTInitToastr.init();
});