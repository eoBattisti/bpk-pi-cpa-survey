const KTNotificationMenu = (function () {
  let notificationMenu;
  let counterElement;
  let counterVisualizedNotifications = 0;
  let counterNotViewedNotifications = 0;
  let notViewedLoading;
  let notViewedContent;
  let visualizedLoading;
  let visualizedContent;
  let csrfToken;
  let notificationAlert;
  let notificationListUrl;
  let timer;
  let firstTab;
  let userId;

  function initVisualizedLoading() {
    $(visualizedLoading).removeClass('d-none');
    $(visualizedContent).addClass('d-none');
  }

  function stopVisualizedLoading() {
    $(visualizedLoading).addClass('d-none');
    $(visualizedContent).removeClass('d-none');
  }

  function initNotViewedLoading() {
    $(notViewedLoading).removeClass('d-none');
    $(notViewedContent).addClass('d-none');
  }

  function stopNotViewedLoading() {
    $(notViewedLoading).addClass('d-none');
    $(notViewedContent).removeClass('d-none');
  }

  function handleCounterChangeEvent() {
    $('[href="#kt_topbar_notifications_not_viewed"]').click(() => {
      $(counterElement).text(counterNotViewedNotifications);
    });
    $('[href="#kt_topbar_notifications_visualized"]').click(() => {
      $(counterElement).text(counterVisualizedNotifications);
    });
  }

  function getNotifications() {
    firstTab.show();

    moment.locale('pt-br');
    let api = notificationMenu.getAttribute('data-api');
    $(counterElement).html(`
      <div class="spinner-grow spinner-grow-sm" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    `);

    initNotViewedLoading();
    initVisualizedLoading();

    // Not Viewed
    fetch(api + getQueryParams(userId, false))
      .then(response => response.json())
      .then(response => {
        counterNotViewedNotifications = response.count;
        $(counterElement).text(response.count);

        $(notViewedContent).html('');

        response.results.forEach(notification => {
          const template = $('<div class="d-flex flex-stack py-4"></div>');

          const body = $(`
            <div class="d-flex align-items-center">
              <div class="mb-0 me-2">
                <a href="${notificationListUrl}" class="fs-6 text-gray-800 text-hover-primary fw-bold d-flex align-items-center">
                  <span class="text-truncate" style="max-width: 180px">${notification.title}</span>
                  <span class="badge badge-light ms-2 fs-8">${moment(notification.created_at).fromNow()}</span>
                </a>
                <div class="text-gray-400 fs-7 text-truncate" style="max-width: 250px">${notification.message}</div>
              </div>
            </div>
          `);

          $(template).append(body);

          $(notViewedContent).append(template);
        });

        if (!response.results.length) {
          $(notificationAlert).addClass('d-none');
          $(notViewedContent).append(`
            <div class="fs-7 text-muted text-center fw-bold">Nenhuma notificação.</div>
          `);
        } else {
          $(notificationAlert).removeClass('d-none');
        }
      })
      .then(() => stopNotViewedLoading())
      .catch(err => {
        console.log(err);
      })

    // Visualized
    fetch(api + getQueryParams(userId, true))
      .then(response => response.json())
      .then(response => {
        counterVisualizedNotifications = response.count;

        $(visualizedContent).html('');

        response.results.forEach(notification => {
          const template = $('<div class="d-flex flex-stack py-4"></div>');
          const body = $(`
            <div class="d-flex align-items-center">
              <div class="mb-0 me-2">
                <a href="${notificationListUrl}" class="fs-6 text-gray-800 text-hover-primary fw-bold d-flex align-items-center">
                  <span class="text-truncate" style="max-width: 180px">${notification.title}</span>
                  <span class="badge badge-light ms-2 fs-8">${moment(notification.created_at).fromNow()}</span>
                </a>
                <div class="text-gray-400 fs-7 text-truncate" style="max-width: 250px">${notification.message}</div>
              </div>
            </div>
          `);

          $(template).append(body);

          $(visualizedContent).append(template);
        });

        if (!response.results.length) {
          $(visualizedContent).append(`
            <div class="fs-7 text-muted text-center fw-bold">Nenhuma notificação.</div>
          `);
        }
      })
      .then(() => stopVisualizedLoading())
      .catch(err => {
        console.log(err);
      })
  }

  function startTimerForNotificationListing() {
    timer = setInterval(() => {
      getNotifications();
    }, 10000);
  }

  function getQueryParams(receiver, visualized) {
    return `?receivers=${receiver}&notificationuser__visualized=${visualized}`;
  }

  return {
    init: function () {
      notificationAlert = document.querySelector('#kt_notification_alert');
      notificationMenu = document.querySelector('#kt_notification_menu');
      csrfToken = notificationMenu.getAttribute('data-csrf');
      userId = notificationMenu.getAttribute('data-user-id');
      notificationListUrl = notificationMenu.getAttribute('data-url-list');
      counterElement = notificationMenu.querySelector('#kt_notification_menu_all');
      notViewedLoading = notificationMenu.querySelector('#kt_topbar_notifications_not_viewed_loading');
      notViewedContent = notificationMenu.querySelector('#kt_topbar_notifications_not_viewed_content');
      visualizedLoading = notificationMenu.querySelector('#kt_topbar_notifications_visualized_loading');
      visualizedContent = notificationMenu.querySelector('#kt_topbar_notifications_visualized_content');

      firstTab = new bootstrap.Tab($('#kt_notification_menu li:first-child a'));

      getNotifications();
      handleCounterChangeEvent();
      startTimerForNotificationListing();
    },
  };
})();

KTUtil.onDOMContentLoaded(function () {
  KTNotificationMenu.init();
});
