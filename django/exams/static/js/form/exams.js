// Stepper lement
var element = document.querySelector("#kt_stepper_example_clickable");

// Initialize Stepper
var stepper = new KTStepper(element);

// Handle navigation click
stepper.on("kt.stepper.click", function (stepper) {
    stepper.goTo(stepper.getClickedStepIndex()); // go to clicked step
});

// Handle next step
stepper.on("kt.stepper.next", function (stepper) {
    stepper.goNext(); // go next step
});

// Handle previous step
stepper.on("kt.stepper.previous", function (stepper) {
    stepper.goPrevious(); // go previous step
});

$("#kt_daterangepicker_2").daterangepicker({
    timePicker: true,
    startDate: moment().startOf("hour"),
    endDate: moment().startOf("hour").add(32, "hour"),
    locale: {
        format: "M/DD hh:mm A"
    }
});

$("#kt_datepicker_3").flatpickr({
    enableTime: true,
    dateFormat: "Y-m-d H:i",
});

$("#kt_datepicker_4").flatpickr({
    enableTime: true,
    dateFormat: "Y-m-d H:i",
});

var element = '#kt_docs_jkanban_fixed_height';

var initjKanban = function () {
    // Get kanban height value
    const kanbanHeight = kanbanEl.getAttribute('data-jkanban-height');

    // Init jKanban
    var kanban = new jKanban({
        element: element,
        gutter: '0',
        widthBoard: '250px',
        boards: [{
            'id': '_fixed_height',
            'title': 'Fixed Height',
            'class': 'primary',
            'item': [
                {
                    'title': '<span class="fw-semibold">Item 1</span>'
                },
                {
                    'title': '<span class="fw-semibold">Item 1</span>'
                },
                {
                    'title': '<span class="fw-semibold">Item 2</span>'
                },
                {
                    'title': '<span class="fw-semibold">Item 3</span>'
                },
            ]
        }
        ],

        // Handle item scrolling
        dragEl: function (el, source) {
            document.addEventListener('mousemove', isDragging);
        },

        dragendEl: function (el) {
            document.removeEventListener('mousemove', isDragging);
        }
    });

    // Set jKanban max height
    const allBoards = kanbanEl.querySelectorAll('.kanban-drag');
    allBoards.forEach(board => {
        board.style.maxHeight = kanbanHeight + 'px';
    });
}

const isDragging = (e) => {
    const allBoards = kanbanEl.querySelectorAll('.kanban-drag');
    allBoards.forEach(board => {
        // Get inner item element
        const dragItem = board.querySelector('.gu-transit');

        // Stop drag on inactive board
        if (!dragItem) {
            return;
        }

        // Get jKanban drag container
        const containerRect = board.getBoundingClientRect();

        // Get inner item size
        const itemSize = dragItem.offsetHeight;

        // Get dragging element position
        const dragMirror = document.querySelector('.gu-mirror');
        const mirrorRect = dragMirror.getBoundingClientRect();

        // Calculate drag element vs jKanban container
        const topDiff = mirrorRect.top - containerRect.top;
        const bottomDiff = containerRect.bottom - mirrorRect.bottom;

        // Scroll container
        if (topDiff <= itemSize) {
            // Scroll up if item at top of container
            board.scroll({
                top: board.scrollTop - 3,
            });
        } else if (bottomDiff <= itemSize) {
            // Scroll down if item at bottom of container
            board.scroll({
                top: board.scrollTop + 3,
            });
        } else {
            // Stop scroll if item in middle of container
            board.scroll({
                top: board.scrollTop,
            });
        }
    });
}
