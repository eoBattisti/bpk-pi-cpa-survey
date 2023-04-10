//BOTAO RESPONSIVO CANCELAR O EIXO

//BOTAO RESPONSIVO ADICIONAR O EIXO
const botaocadastroeixo = document.getElementById('AdicionarEixo');

botaocadastroeixo.addEventListener('click', e =>{
    e.preventDefault();

    Swal.fire({
        text: "Adicionado com sucesso!",
        icon: "success",
        buttonsStyling: false,
        confirmButtonText: "Okay",
        customClass: {
            confirmButton: "btn btn-primary"
        }
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = "http://localhost:8000/eixos/list/";
            const botaoSubmit = document.querySelector('[name="id_submiteixo_name"]');
            botaoSubmit.click();
        }
    });
});

const botaocancelareixo = document.getElementById('CancelarCadastroEixo');

botaocancelareixo.addEventListener('click', e =>{
    e.preventDefault();
    Swal.fire({
        html: `Deseja mesmo cancelar o cadastro/edição?`,
        icon: "info",
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
            window.location.href = "http://localhost:8000/eixos/list/";
        }
    });
});