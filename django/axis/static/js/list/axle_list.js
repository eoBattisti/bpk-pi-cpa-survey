

//TABELA DE EIXO SCROLLBAR
$("#kt_datatable_fixed_columns").DataTable({
	scrollY:        "auto", // Define a altura da tabela como "auto"
	scrollX:        true,
	scrollCollapse: true,
	fixedColumns:   {
		left: 2
	},
	paging: true,
	pageLength: 10
});
//TABELA DE EIXO SCROLLBAR

//DESEJA APAGAR O EIXO CADASTRADO?



$('button[name="ApagarEixo"]').on('click', function (e){
    e.preventDefault();

    let config = {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": $(this).data('csrf-token')
        },
    }

    Swal.fire({
        html: `Deseja mesmo excluir este  cadastro?`,
        icon: "warning",
        buttonsStyling: false,
        showCancelButton: true,
        confirmButtonText: "Sim",
        cancelButtonText: 'Não',
        customClass: {
            confirmButton: "btn btn-primary",
            cancelButton: 'btn btn-danger'
        }
    }).then((result) => {
        if (result.isConfirmed) {
            let api = $(this).data('delete-url');
            fetch(api, config)
            .then(response => {
                console.log(response.status)
                if(response.status != 204){
                    return toastr.error('Error')
                }
                return toastr.success('Eixo excluído com sucesso!')
            }).finally(() => {
                setTimeout(() => {
                window.location.reload()
            }, 1200);
            })
        }
    });
});