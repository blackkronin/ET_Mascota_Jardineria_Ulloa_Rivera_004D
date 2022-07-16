const contacto = document.getElementById('contacto');
const inputs = document.querySelectorAll('#contacto input');

const expresiones = {
    nombreape: /^[a-zA-ZÀ-ÿ\s]{1,40} [a-zA-ZÀ-ÿ\s]{1,40}$/, //desde 1 a 50 caracteres de longitud y formato 'Nombre Apellido'.
    correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/, //simbolos permitidos letras.
    celular: /^\d{7,14}$/, //de 7 a 14 números.
    rut: /^[0-9]{9}$/ //de 9 numeros del rut sin guión con digito verificador.
}

const campos={
    nombreape: false,
    correo: false,
    celular: false,
    rut: false
}

const validarContacto= (e) => {
    switch (e.target.name){
        case "nombreape":
            validarCampo(expresiones.nombreape,e.target,'nombreape')
        break;
        case "correo":
            validarCampo(expresiones.correo,e.target,'correo')
        break;
        case "celular":
            validarCampo(expresiones.celular,e.target,'celular')
        break;
        case "rut":
            validarCampo(expresiones.rut,e.target,'rut')
        break;
        
    }
}

const validarCampo = (expresion,input,campo) => {
    if(expresion.test(input.value)){
        document.getElementById(`grupo__${campo}`).classList.remove('contacto__grupo-incorrecto');
        document.getElementById(`grupo__${campo}`).classList.add('contacto__grupo-correcto');
        document.querySelector(`#grupo__${campo} i`).classList.add('fa-check-circle');
        document.querySelector(`#grupo__${campo} i`).classList.remove('fa-times-circle');
        document.querySelector(`#grupo__${campo} .contacto__input-error`).classList.remove('contacto__input-error-activo');
        campos[campo]=true;
    }
    else{
        document.getElementById(`grupo__${campo}`).classList.add('contacto__grupo-incorrecto');
        document.getElementById(`grupo__${campo}`).classList.remove('contacto__grupo-correcto');
        document.querySelector(`#grupo__${campo} i`).classList.add('fa-times-circle');
        document.querySelector(`#grupo__${campo} i`).classList.remove('fa-check-circle');
        document.querySelector(`#grupo__${campo} .contacto__input-error`).classList.add('contacto__input-error-activo');
        campos[campo]=false;
    }
}

inputs.forEach((input) =>{
    input.addEventListener('keyup', validarContacto);
    input.addEventListener('blur', validarContacto);
});



contacto.addEventListener('submit',(e) => {
    e.preventDefault;

    if(campos.nombreape && campos.correo && campos.celular && campos.rut){
        contacto.reset();
        document.getElementById('contacto__mensaje-exito').classList.add('contacto__mensaje-exito-activo');
        setTimeout(()=>{
            document.getElementById('contacto__mensaje-exito').classList.remove('contacto__mensaje-exito-activo');
        },5000);
        document.querySelectorAll('.contacto__grupo-correcto').forEach((icono)=>{
            icono.classList.remove('contacto__grupo-correcto');
        });
    }
    else{
        document.getElementById('contacto__mensaje').classList.add('contacto__mensaje-activo');
        setTimeout(()=>{
            document.getElementById('contacto__mensaje').classList.remove('contacto__mensaje-activo');
        },5000);
    }
});