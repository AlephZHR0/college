//usuarios.js

const url_base = "http://127.0.0.1:5000/usuario";

async function buscarTodosOsUsuarios() {
    const resposta = await fetch(`${url_base}/`);
    const usuarios = await resposta.json();
    const corpoTabela = document.getElementById('tabelaUsuarios').getElementsByTagName('tbody')[0];

    // Limpar linhas existentes
    corpoTabela.innerHTML = '';

    usuarios.forEach(usuario => {
        const novaLinha = corpoTabela.insertRow();
        novaLinha.insertCell(0).innerText = usuario.user_id;
        novaLinha.insertCell(1).innerText = usuario.name;
        novaLinha.insertCell(2).innerText = usuario.email;
        novaLinha.insertCell(3).innerText = usuario.user_name;
        novaLinha.insertCell(4).innerText = usuario.password;
    
        // Botões de ação
        const colunaAcoes = novaLinha.insertCell(5);
        const btnEditar = document.createElement("button");
        btnEditar.innerText = "Editar";
        btnEditar.onclick = () => editarUsuario(usuario.user_id);
        colunaAcoes.appendChild(btnEditar);
    
        const btnRemover = document.createElement("button");
        btnRemover.innerText = "Remover";
        btnRemover.onclick = () => removerUsuario(usuario.user_id);
        colunaAcoes.appendChild(btnRemover);
    });
}

async function adicionarUsuario(evento) {
    evento.preventDefault();

    const nome = document.getElementById('nome').value;
    const email = document.getElementById('email').value;
    const user_name = document.getElementById('user_name').value;
    const password = document.getElementById('password').value;


    const resposta = await fetch(`${url_base}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name: nome, email: email , user_name: user_name, password: password})
    });

    if (resposta.status === 201) {
        // Limpar o formulário e buscar todos os usuários novamente para atualizar a tabela
        document.getElementById('formularioAdicionarUsuario').reset();
        buscarTodosOsUsuarios();
    } else {
        console.error('Falha ao adicionar usuário. Servidor respondeu com', resposta.status);
    }
}

async function editarUsuario(userID) {
    const nome = prompt("Novo nome:");
    const email = prompt("Novo email:");
    const user_name = prompt("Novo user_name:");
    const password = prompt("Nova senha:");

    if (nome && email && user_name && password) {
        const resposta = await fetch(`${url_base}/${userID}/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name: nome, email: email , user_name: user_name, password: password})
        });

        if (resposta.status === 200) {
            buscarTodosOsUsuarios();
        } else {
            console.error('Falha ao editar usuário. Servidor respondeu com', resposta.status);
        }
    }
}

async function removerUsuario(userID) {
    const confirmacao = confirm("Tem certeza que deseja remover este usuário?");
    if (confirmacao) {
        const resposta = await fetch(`${url_base}/${userID}/`, {
            method: 'DELETE'
        });

        if (resposta.status === 200) {
            buscarTodosOsUsuarios();
        } else {
            console.error('Falha ao remover usuário. Servidor respondeu com', resposta.status);
        }
    }
}


document.getElementById('formularioAdicionarUsuario').addEventListener('submit', adicionarUsuario);
buscarTodosOsUsuarios();
