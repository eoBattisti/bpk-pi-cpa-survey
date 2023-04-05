

//TABELA DE EIXO SCROLLBAR
$("#kt_datatable_fixed_columns").DataTable({
	scrollY:        "300px",
	scrollX:        true,
	scrollCollapse: true,
	fixedColumns:   {
		left: 2
	}
});
//TABELA DE EIXO SCROLLBAR

//DESEJA APAGAR O EIXO CADASTRADO?
const excluireixo = document.getElementById('ApagarEixo');

excluireixo.addEventListener('click', e =>{
    e.preventDefault();

    let config = {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": excluireixo.getAttribute('data-csrf-token')
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
            let api = excluireixo.getAttribute('data-delete-url');
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