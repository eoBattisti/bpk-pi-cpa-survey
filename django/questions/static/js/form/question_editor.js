
const botaocancelarpergunta = document.getElementById('CancCad');

botaocancelarpergunta.addEventListener('click', e => {
    e.preventDefault();
    Swal.fire({
        html: `Informações inseridas serão perdidas. Deseja mesmo cancelar?`,
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
            window.location.href = "http://localhost:8000/perguntas/list/";
        }
    });
});

const botaocadastropergunta = document.getElementById('AddPerg');

botaocadastropergunta.addEventListener('click', e => {
    e.preventDefault();

    const eixo = document.querySelector('#id_axis')
    const descricao = document.querySelector('#id_description')
    const erro1 = document.querySelector('#erro1')
    const erro2 = document.querySelector('#erro2')
    erro1.style.color = "red";
    erro2.style.color = "red";

    if(!eixo.value && !descricao.value) {

        erro1.textContent = '* Selecione um eixo.';
        erro2.textContent = '* Adicione uma descrição.';
        
        Swal.fire({
            text: "Alguns erros foram detectados. Por favor, tente novamente.",
            icon: "error",
            buttonsStyling: false,
            confirmButtonText: "Entendi!",
            customClass: {
                confirmButton: "btn btn-primary"
            }
        })
        return;
    } else if(!eixo.value) {

        erro1.textContent = '* Selecione um eixo.';
        
        Swal.fire({
            text: "Alguns erros foram detectados. Por favor, tente novamente.!",
            icon: "error",
            buttonsStyling: false,
            confirmButtonText: "Entendi!",
            customClass: {
                confirmButton: "btn btn-primary"
            }
        })
        return;
    } else if(!descricao.value) {

        erro2.textContent = '* Adicione uma descrição.';
        
        Swal.fire({
            text: "Alguns erros foram detectados. Por favor, tente novamente.",
            icon: "error",
            buttonsStyling: false,
            confirmButtonText: "Entendi!",
            customClass: {
                confirmButton: "btn btn-primary"
            }
        })
        return;
    }

    Swal.fire({
        text: "Informações cadastradas com sucesso!",
        icon: "success",
        buttonsStyling: false,
        confirmButtonText: "Ok!",
        customClass: {
            confirmButton: "btn btn-primary"
        }
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = "http://localhost:8000/perguntas/list/";
            const botaoSubmit = document.querySelector('[name="id_submitperg_name"]');
            botaoSubmit.click();
        } 
    });
});

