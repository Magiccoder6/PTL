import { callAPI, showToast } from "./misc.js";

document.addEventListener('DOMContentLoaded', function() {
    
    document.getElementById('login_form').addEventListener('submit', function(event) {
        event.preventDefault();
        var formData = new FormData(this);

        callAPI('POST', '/login', formData).then(()=>{
            showToast("Login success", 'success')
        }).catch((e)=>{
            showToast(e, 'danger')
        })
        
    });

    document.getElementById('register_form').addEventListener('submit', function(event) {
        event.preventDefault();
        var formData = new FormData(this);

        callAPI('POST', '/register', formData).then(()=>{
            showToast('Registered successfully', 'success')
        }).catch((e)=>{
            showToast(e, 'danger')
        })
        
    });
});