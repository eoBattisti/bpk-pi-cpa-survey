const KTSearchHorizontal = (function () {
  let form;
  let advancedSearchToggle;
  let advancedSearchKeywords;
  let selectOrderByEl;
  let search;
  let showGrid = false;
  let orderBy = 1;
  let currentPage = 1;
  let pageSize = 9;
  let numberOfPages;
  let submitSearch;
  let tagifyAdvancedSearchKeywords;
  let hasFilters;
  let copySearch;
  let lastSearch = null;

  let categories = {
    'company': 0,
    'event': 1,
    'service': 2,
    'product': 3,
    'third_party': 4,
    'all': 5,
  };

  let searchCardHeader;
  let nextEventsContainer;
  let hasAlreadyBeenSearched = false;

  let api;
  let keywordsAPI;
  let csrfToken;

  const spinnerLoading = `
    <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
    <span class="ms-3">Loading...</span>
  `;

  const emptyCardResults = `
    <div class="col text-center">
      <span class="fs-2 text-muted fw-bold">
        Nenhum resultado foi encontrado.
      </span>
    </div>
  `;

  const emptyTableResults = `
    <tr>
      <td colspan="4" class="text-center">
        <span class="fs-5 text-muted fw-bold">Nenhum resultado foi encontrado.</span>
      </td>
    </tr>
  `;



  // Init Functions
  function initSelectOrderBy() {
    let selectOrderBy = $(selectOrderByEl).select2({
      minimumResultsForSearch: -1,
    });

    selectOrderBy.on('select2:select', function (e) {
      orderBy = e.params.data.id;
      getResults(currentPage);

      let orderResults = document.getElementById('kt_order_results');

      if (orderBy == 1) {
        orderResults.innerText = 'por Atualizações Recentes ↓';
      } else {
        orderResults.innerText = 'por Mais antigos ↓';
      }
    });
  }

  function initAdvancedSearchForm() {
    const config = {
      templates: {
        tag: function (tagData) {
          return `
            <tag title='${tagData.value}' contenteditable='false' spellcheck='false'
              class='tagify__tag tagify--noAnim tagify__tag--primary ${tagData.class ? tagData.class : ""}' ${this.getAttributes(tagData)}>
              <x title="remove tag" class="tagify__tag__removeBtn"></x>
              <div>
                <span class='tagify__tag-text'>${tagData.value}</span>
              </div>
            </tag>
          `;
        },
      },
      originalInputValueFormat: listValues => listValues.map(item => item.value)
    };
    tagifyAdvancedSearchKeywords = new Tagify(advancedSearchKeywords, config);
    tagifyAdvancedSearchKeywords.on('change', function (e) {
      getResults(currentPage);
    });
  }

  function initSearch() {
    let initiated = submitSearch.getAttribute('data-initiated');
    initiated = initiated == 'true';

    if (initiated || hasFilters) {
      getResults(currentPage);
    } else {
      let nextEventsContainer = document.querySelector('#kt_next_events_container');
      if (nextEventsContainer != null) {
        nextEventsContainer.classList.remove('d-none');
      }
    }
  }

  function initActivitySelect() {
    const config = {
      placeholder: 'Selecione uma opção',
      allowClear: true,
    };
    const select = document.querySelector('[name="activity"]');
    $(select).select2(config);
    $(select).on('select2:select', function (e) {
      getResults(currentPage);
    });
    $(select).on('select2:clear', function (e) {
      getResults(currentPage);
    });
  }

  function initSearchPage() {
    if (document.location.search != '' && document.location.search != null) {
      let params = new URLSearchParams(document.location.search);
      hasFilters = false;

      if (params.get('search') != null) {
        search.value = params.get('search');
        hasFilters = true;
      }

      if (params.get('keywords') != null) {
        advancedSearchKeywords.value = params.get('keywords');
        hasFilters = true;
      }

      if (params.get('type') != null) {
        if (params.get('type') == '5') {
          document.querySelector('[value="all"]').checked = true;
          hasFilters = true;
        } else if (params.get('type') == '0') {
          document.querySelector('[value="company"]').checked = true;
          hasFilters = true;
        } else if (params.get('type') == '2') {
          document.querySelector('[value="service"]').checked = true;
          hasFilters = true;
        } else if (params.get('type') == '3') {
          document.querySelector('[value="product"]').checked = true;
          hasFilters = true;
        } else if (params.get('type') == '1') {
          document.querySelector('[value="event"]').checked = true;
          hasFilters = true;
        } else if (params.get('type') == '4') {
          document.querySelector('[value="third_party"]').checked = true;
          hasFilters = true;
        }
      }

      if (params.get('activity') != null) {
        document.querySelector('[name="activity"]').value = params.get('activity');
        hasFilters = true;
      }

      if (params.get('page_size') != null) {
        pageSize = Number.parseInt(params.get('page_size'));
      }

      if (params.get('status') != null) {
        orderBy = Number.parseInt(params.get('status'));
        selectOrderByEl.value = orderBy;
      }
    }
  }



  // HTTP Requests
  function getHTTPRequest(params) {
    let config = {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken,
      },
    };

    let button = document.getElementById('kt_spinner_loading_button');
    button.innerHTML = spinnerLoading;
    return fetch(api + params, config)
      .then(response => {
        if (!response.ok) {
          throw new Error(response.statusText)
        }
        return response;
      })
      .then(response => response.json())
      .catch(err => {
        toastr.error('Houve um erro. Tente novamente!');
        console.log(err);
      })
      .finally(() => {
        button.innerHTML = 'Buscar';
      });
  }

  function getKeywordsHTTPRequest() {
    let config = {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    };

    return fetch(keywordsAPI, config)
      .then(response => {
        if (!response.ok) {
          throw new Error(response.statusText)
        }
        return response;
      })
      .then(response => response.json())
      .catch(err => {
        toastr.error('Houve um erro ao criar a nuvem de palavras.');
        console.log(err);
      });
  }



  // Util Functions
  function getParams(values) {
    const params = new Object();

    if (values['search'] != null) {
      params['search'] = values['search'];
    }

    if (values['keywords'] != null) {
      params['keywords'] = values['keywords'];
    }

    if (values['type'] != null) {
      if (categories[values['type']] != null) {
        params['type'] = categories[values['type']];
      }
    }

    if (values['activity'] != null) {
      params['activity'] = values['activity'];
    }

    if (values['page'] != 1 && values['page'] != null) {
      params['page'] = values['page'];
    }

    params['page_size'] = pageSize;
    params['status'] = orderBy;
    params['archived'] = false;

    let queryParams = new URLSearchParams(params);
    return queryParams.toString().length > 0 ? '?' + queryParams : '';
  }

  function createCardElement(result) {
    const firstLetter = result.title[0];

    let body = '';
    if (result.search_type == 0) {
      body = `
        <div class="border border-gray-300 border-dashed w-100 h-100px rounded min-w-80px p-2 border-box">
          <div class="text-gray-500 h-100 overflow-y-scroll">${result.search_description}</div>
        </div>
      `;
    } else if (result.search_type == 1) {
      let sections = result.section_detail.filter(section => section.section_type == 6);
      let items = '';

      if (sections.length == 0) {
        items = `
          <div class="border border-gray-300 h-100 border-dashed rounded min-w-80px p-2 border-box d-flex flex-column justify-content-center align-items-center">
            <div class="fs-6 fw-bold text-gray-700 text-center ellipsis-line ellipsis-one-line">Sem Destaques</div>
          </div>
        `;
      } else {
        sections.forEach(section => {
          items += `
            <div class="border border-gray-300 h-100 border-dashed rounded min-w-80px p-2 border-box d-flex flex-column justify-content-center align-items-center">
              <div class="fs-6 fw-bold text-gray-700 text-center ellipsis-line ellipsis-one-line">${section.content.value}</div>
              <div class="fw-semibold text-gray-400 text-center ellipsis-line ellipsis-three-line">${section.content.description}</div>
            </div>
          `;
        });
      }

      body = `
        <div class="grid-container w-100 h-100px p-0">
          ${items}
        </div>
      `;
    }

    let padding = 'p-9';
    let containerPeriod = '';

    if (result.category == 1) {
      padding = 'pt-9 ps-9 pe-9 pb-2';

      let start = new moment(result.event_detail.start).format('YYYY-MM-DD HH:mm');
      let end = new moment(result.event_detail.end).format('YYYY-MM-DD HH:mm');

      if (start != null) {
        containerPeriod = `
          <div class="justify-content-between mt-1 w-100 d-flex">
            <div class="text-muted">
              <i class="fa-regular fa-calendar"></i>
              <span>${start}</span>
            </div>

            <div><i class="fa-solid fa-arrow-right"></i></div>

            <div class="text-muted">
              <i class="fa-regular fa-calendar"></i>
              <span>${end}</span>
            </div>
          </div>
        `;
      }
    }

    let ribbon = '';
    let color = 'primary';
    let path = '';
    if (result.category == 0) {
      color = 'primary';
      ribbon = `
        <div class="ribbon-label bg-primary">
          Empresa
        </div>
      `;
      path = `/${result.company_detail.fantasy_name_slug}/${result.path}`;
    } else if (result.category == 3) {
      color = 'info';
      ribbon = `
        <div class="ribbon-label bg-info">
          Produto
        </div>
      `;
      path = `/${result.company_detail.fantasy_name_slug}/produtos/${result.path}`;
    } else if (result.category == 2) {
      color = 'warning';
      ribbon = `
        <div class="ribbon-label bg-warning">
          Serviço
        </div>
      `;
      path = `/${result.company_detail.fantasy_name_slug}/servicos/${result.path}`;
    } else if (result.category == 4) {
      color = 'warning';
      ribbon = `
        <div class="ribbon-label bg-warning">
          BPK Indica
        </div>
      `;
      path = `/${result.company_detail.fantasy_name_slug}/servicos/${result.path}`;
    } else {
      color = 'success';
      ribbon = `
        <div class="ribbon-label bg-success">
          Evento
        </div>
      `;
      path = `/${result.company_detail.fantasy_name_slug}/eventos/${result.path}`;
    }

    let header;
    if (result.logo_sm != null) {
      header = `
        <a href="${path}" class="symbol symbol-65px symbol-2by3 mb-5">
          <img src="${result.logo_sm}" alt="image" class="${result.adjust_search_image ? 'object-fit-fill' : 'object-fit-cover'}">
        </a>
      `;
    } else {
      header = `
        <a href="${path}" class="symbol symbol-65px symbol-2by3 mb-5">
          <span class="symbol-label fs-2x fw-semibold text-${color} bg-light-${color}">${firstLetter}</span>
        </a>
      `;
    }

    const templateCard = `
      <div class="col-md-6 col-xxl-4">
        <div class="card">
          <div class="card-body d-flex flex-center flex-column ${padding} ribbon ribbon-top">
            ${ribbon}

            ${header}

            <a href="${path}" class="fs-4 text-gray-800 text-hover-${color} fw-bold mb-0 cursor-pointer ellipsis-text" title="${result.search_title}"
              style="max-width: 342px">
              ${result.search_title}
            </a>

            <span class="badge badge-light-dark mb-3">${result.company_detail.fantasy_name}</span>

            ${body}

            ${containerPeriod}
          </div>
        </div>
      </div>
    `;

    return templateCard;
  }

  function createTableRowElement(result) {
    const firstLetter = result.title[0];

    let body = '';
    if (result.search_type == 0) {
      body = `
        <td class="fw-light fs-7 text-gray-600 w-500px">
          <div class="text-truncate" style="width: 500px">
            ${result.search_description}
          </div>
        </td>
      `;
    } else if (result.search_type == 1) {
      let sections = result.section_detail.filter(section => section.section_type == 6);
      let items = '';

      if (sections.length == 0) {
        items = `
          <div>
            <div class="w-100 text-center">Sem destaques</div>
          </div>
        `;
      } else {
        sections.forEach(section => {
          items += `
            <div class="d-flex flex-column align-items-start border border-gray-300 border-dashed rounded min-w-80px py-3 px-2 mx-1" style="box-sizing: border-box;">
              <div class="fs-6 fw-bold text-gray-700">${section.content.value}</div>
              <div class="fw-semibold text-gray-400">${section.content.description}</div>
            </div>
          `;
        });
      }

      body = `
        <td class="fw-light fs-7 text-gray-600 w-500px">
          <div class="d-flex">
            ${items}
          </div>
        </td>
      `;
    }

    let containerPeriod = '';

    if (result.category == 1) {
      let start = new moment(result.event_detail.start).format('YYYY-MM-DD HH:mm');
      let end = new moment(result.event_detail.end).format('YYYY-MM-DD HH:mm');

      if (start != null) {
        containerPeriod = `
          <div class="text-muted fs-9 mt-1">
            <span>${start}</span>
            <span class="mx-1"><i class="fa-solid fa-arrow-right"></i></span>
            <span>${end}</span>
          </div>
        `;
      }
    }

    let color = 'primary';
    let category;
    let path = '';
    if (result.category == 0) {
      color = 'primary';
      category = 'Empresa';
      path = `/${result.company_detail.fantasy_name_slug}/${result.path}`;
    } else if (result.category == 3) {
      color = 'info';
      category = 'Produto';
      path = `/${result.company_detail.fantasy_name_slug}/produtos/${result.path}`;
    } else if (result.category == 2) {
      color = 'warning';
      category = 'Serviço';
      path = `/${result.company_detail.fantasy_name_slug}/servicos/${result.path}`;
    } else if (result.category == 4) {
      color = 'warning';
      category = 'BPK Indica';
      path = `/${result.company_detail.fantasy_name_slug}/servicos/${result.path}`;
    } else {
      color = 'success';
      category = 'Evento';
      path = `/${result.company_detail.fantasy_name_slug}/eventos/${result.path}`;
    }

    let header;
    if (result.logo_sm != null) {
      header = `
        <a href="${path}" class="symbol symbol-2by3 symbol-45px">
          <img src="${result.logo_sm}" alt="image" class="${result.adjust_search_image ? 'object-fit-fill' : 'object-fit-cover'}">
        </a>
      `;
    } else {
      header = `
        <a href="${path}" class="symbol symbol-2by3 symbol-45px">
          <span class="symbol-label bg-light-${color} text-${color} fw-semibold">${firstLetter}</span>
        </a>
      `;
    }

    const templateRow = `
      <tr>
        <td>
          <div class="d-flex align-items-center">
            <div class="me-5 position-relative">
              ${header}
            </div>
            <div class="d-flex flex-column justify-content-center">
              <a href="${path}" class="mb-1 text-gray-700 fs-6 text-hover-${color}">
                ${result.title}
              </a>
              <div class="fw-semibold text-gray-400 text-truncate">${result.search_title}</div>
              ${containerPeriod}
            </div>
          </div>
        </td>
        <td class="text-center">
          <span class="text-muted">${result.company_detail.fantasy_name}</span>
        </td>
        <td class="text-center">
          <span class="badge badge-light-${color} badge-sm fw-bold">${category}</span>
        </td>
        ${body}
        <td class="text-end">
          <a href="${path}" class="btn btn-light btn-sm">Ver</a>
        </td>
      </tr>
    `;

    return templateRow;
  }

  function formatEventDatetimes() {
    datetimeContainers = document.querySelectorAll('.kt_event_datetime_container');

    datetimeContainers.forEach(container => {
      let startContainer = container.querySelector('.kt_event_datetime .kt_event_datetime_start');
      let endContainer = container.querySelector('.kt_event_datetime .kt_event_datetime_end');

      startContainer.innerHTML = new moment(startContainer.innerText).format('YYYY-MM-DD HH:mm');
      endContainer.innerHTML = new moment(endContainer.innerText).format('YYYY-MM-DD HH:mm');

      container.querySelector('.kt_event_datetime').classList.remove('d-none');
      container.querySelector('.kt_event_datetime').classList.add('d-flex');

      container.querySelector('.kt_event_datetime_loading').classList.add('d-none');
    });
  }



  // Handle Events
  function handleAdvancedSearchToggle() {
    advancedSearchToggle.addEventListener('click', function (e) {
      e.preventDefault();

      if (!advancedSearchToggle.classList.contains('collapsed')) {
        advancedSearchToggle.innerHTML = `
          Filtros
          <span class="svg-icon svg-icon-3 m-0 ms-2">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12.5657 11.3657L16.75 15.55C17.1642 15.9643 17.8358 15.9643 18.25 15.55C18.6642 15.1358 18.6642 14.4643 18.25 14.05L12.7071 8.50716C12.3166 8.11663 11.6834 8.11663 11.2929 8.50715L5.75 14.05C5.33579 14.4643 5.33579 15.1358 5.75 15.55C6.16421 15.9643 6.83579 15.9643 7.25 15.55L11.4343 11.3657C11.7467 11.0533 12.2533 11.0533 12.5657 11.3657Z" fill="currentColor"/>
            </svg>
          </span>
        `;
      } else {
        advancedSearchToggle.innerHTML = `
          Filtros
          <span class="svg-icon svg-icon-3 m-0 ms-2">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M11.4343 12.7344L7.25 8.55005C6.83579 8.13583 6.16421 8.13584 5.75 8.55005C5.33579 8.96426 5.33579 9.63583 5.75 10.05L11.2929 15.5929C11.6834 15.9835 12.3166 15.9835 12.7071 15.5929L18.25 10.05C18.6642 9.63584 18.6642 8.96426 18.25 8.55005C17.8358 8.13584 17.1642 8.13584 16.75 8.55005L12.5657 12.7344C12.2533 13.0468 11.7467 13.0468 11.4343 12.7344Z" fill="currentColor"/>
            </svg>
          </span>
        `;
      }
    });
  }

  function handleSubmitEvent() {
    const clickEvent = () => {
      getResults(currentPage);
    }
    submitSearch.addEventListener('click', clickEvent);

    const keyUpEvent = (e) => {
      if (e.key == 'Enter') {
        getResults(currentPage);
      }
    }
    search.addEventListener('keyup', keyUpEvent);
  }

  function handleTypeSelectEvent() {
    const event = function (e) {
      getResults(currentPage);
    };
    types = document.querySelectorAll('[name="type"]');
    types.forEach(type => {
      type.addEventListener('click', event);
    });
  }

  function handleCopySearchEvent() {
    const event = function (e) {
      navigator.clipboard.writeText(document.location.href);
    }
    copySearch.addEventListener('click', event);
  }



  // Search Functions
  function getResults(page) {
    let values = {
      search: search.value || null,
      keywords: advancedSearchKeywords.value || null,
      type: document.querySelector('[name="type"]:checked').value || null,
      activity: document.querySelector('[name="activity"]').value || null,
      page: currentPage,
    };

    if (lastSearch == null) {
      lastSearch = values;
    } else {
      if (lastSearch.search != values.search || lastSearch.keywords != values.keywords || lastSearch.type != values.type || lastSearch.activity != values.activity) {
        currentPage = 1;
        values.page = currentPage;
        lastSearch = values;
      }
    }

    const params = getParams(values);

    getHTTPRequest(params)
      .then(response => {
        if (!hasAlreadyBeenSearched) {
          hasAlreadyBeenSearched = true;
          searchCardHeader.classList.add('d-none');

          if (nextEventsContainer != null) {
            nextEventsContainer.classList.add('d-none');
          }
        }

        if (!showGrid) {
          showGrid = true;
          document.getElementById('kt_result_body').classList.remove('d-none');
        }

        let minItems = 0;
        let maxItems = 0;
        numberOfPages = response.total_pages;

        if (response.count != 0) {
          minItems = (currentPage * pageSize) - (pageSize - 1);
          maxItems = response.count;
        }

        document.getElementById('kt_current_page_min').innerText = minItems;
        document.getElementById('kt_current_page_max').innerText = maxItems;
        document.getElementById('kt_counter_results').innerText = response.count;
        document.getElementById('kt_total_items').innerText = response.count;

        updatePagination();

        const cardResults = document.getElementById('kt_search_card_pane_results');
        const tableResults = document.getElementById('kt_search_table_pane_results');

        if (response.results.length == 0) {
          cardResults.innerHTML = emptyCardResults;
          tableResults.innerHTML = emptyTableResults;
        } else {
          cardResults.innerHTML = '';
          tableResults.innerHTML = '';

          response.results.forEach(result => {
            let templateCard = createCardElement(result);
            let templateRow = createTableRowElement(result);

            cardResults.innerHTML += templateCard;
            tableResults.innerHTML += templateRow;
          });
        }
      })
      .then(() => {
        let initiated = submitSearch.getAttribute('data-initiated');
        initiated = initiated == 'true' ? '&initialized=true' : '';

        window.history.replaceState('', '', params + initiated);
      });
  }

  function updatePagination() {
    const pagination = document.getElementById('kt_pagination');
    pagination.innerHTML = '';

    let previousButton = document.createElement('li');
    previousButton.classList = 'page-item previous';
    previousButton.innerHTML = `
      <a class="page-link">
        <i class="previous"></i>
      </a>
    `;

    let nextButton = document.createElement('li');
    nextButton.classList = 'page-item next text-hover';
    nextButton.innerHTML = `
      <a class="page-link">
        <i class="next"></i>
      </a>
    `;

    if (currentPage > 1) {
      previousButton.addEventListener('click', () => {
        currentPage--;
        getResults(currentPage);
      });
      previousButton.classList.add('cursor-pointer');
    } else {
      previousButton.classList.add('disabled');
    }

    if (currentPage < numberOfPages) {
      nextButton.addEventListener('click', () => {
        currentPage++;
        getResults(currentPage);
      });
      nextButton.classList.add('cursor-pointer');
    } else {
      nextButton.classList.add('disabled');
    }

    pagination.appendChild(previousButton);

    let interval = 3;

    for (let i = 1; i <= numberOfPages; i++) {
      let page = document.createElement('li');
      page.classList = `page-item ${i == currentPage ? 'active' : ''}`;
      page.innerHTML = `<a class="page-link">${i}</a>`;

      let ellipsis = false;

      if (i != numberOfPages) {
        if (i == currentPage + interval) {
          page = document.createElement('li');
          page.classList = `page-item`;
          page.innerHTML = '<div class="page-link">...</div>';
          ellipsis = true;
        } else if (i > currentPage + interval && i != numberOfPages) {
          page = null;
        }
      }

      if (i != 1) {
        if (i == currentPage - interval) {
          page = document.createElement('li');
          page.classList = `page-item`;
          page.innerHTML = '<div class="page-link">...</div>';
          ellipsis = true;
        } else if (i < currentPage - interval) {
          page = null;
        }
      }

      if (currentPage != i && page != null && !ellipsis) {
        page.addEventListener('click', () => {
          currentPage = i;
          getResults(currentPage);
        });
        page.classList.add('cursor-pointer');
      }

      if (page != null) {
        pagination.appendChild(page);
      }
    }

    pagination.appendChild(nextButton);
  }

  function getKeywords() {
    getKeywordsHTTPRequest().then(response => {
      let svg = d3.select("#word-cloud").append("g");

      let colors = [
        '#A1A5B7',
        '#A1A5B7',
        '#aee239',
        // '#9bb0cc',
        '#95b4de',
        '#7aaaeb'
      ];

      let list = new Array();
      response.forEach(keyword => {
        list.push({
          text: keyword.word.charAt(0).toUpperCase() + keyword.word.slice(1).toLowerCase(),
          count: keyword.rank,
          color: colors[Math.round(keyword.rank / 2 * 10)] || '#009ef7',
        });
      });

      let fill = d3.scaleOrdinal(d3.schemeCategory20);
      let size = d3.scaleLinear().range([0, 20]).domain([0, d3.max(list, d => d.count)]);

      let width = 600;
      let height = 175;

      let wordCloudData = list.map(function (d) {
        return { text: d.text, size: 7.5 + size(d.count) * 0.5, color: d.color };
      });

      let layout = d3.layout.cloud()
        .size([width, height])
        .words(wordCloudData)
        .padding(4)
        .rotate(0)
        .text(d => d.text)
        .font('Inter')
        .fontSize(d => d.size)
        .on("end", draw);

      layout.start();

      function draw(words) {
        svg.append("g")
          .attr("transform", `translate(${width/2},${height/2})`)
          .selectAll("text")
          .data(words)
          .enter().append("text")
          .style("fill", (d, i) => { /*d.color = '#A1A5B7';*/ return d.color; })
          .style("text-anchor", "middle")
          .attr("transform", d => "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")")
          .attr("class", "word-text")
          .attr('font-family', 'Inter')
          .text(d => d.text)
          .on("click", function (d) {
            search.value = d.text;
            getResults();
          })
          .style("font-size", d => d.size + "px");
      }
    });
  }



  return {
    init: function () {
      const element = document.querySelector('#kt_app_content');
      form = document.querySelector('#kt_search_form');

      advancedOptions = element.querySelector('#kt_advanced_search_options');
      advancedSearchToggle = element.querySelector('#kt_horizontal_search_advanced_link');
      advancedSearchKeywords = advancedOptions.querySelector('#kt_advanced_search_keywords');
      submitSearch = document.querySelector('#kt_submit_search');
      selectOrderByEl = document.querySelector('#kt_select_order_by');
      search = document.querySelector('#kt_text_search');
      searchCardHeader = document.querySelector('#kt_search_card_header');
      nextEventsContainer = document.querySelector('#kt_next_events_container');
      copySearch = document.querySelector('#kt_copy_search');

      api = form.getAttribute('data-api');
      keywordsAPI = form.getAttribute('data-keywords-api');
      csrfToken = form.getAttribute('data-csrf');

      initSearchPage();

      initAdvancedSearchForm();
      initSelectOrderBy();
      initActivitySelect();

      handleAdvancedSearchToggle();
      handleSubmitEvent();
      handleTypeSelectEvent();
      handleCopySearchEvent();

      initSearch();

      formatEventDatetimes();
    },
  };
})();

KTUtil.onDOMContentLoaded(function () {
  KTSearchHorizontal.init();
});
