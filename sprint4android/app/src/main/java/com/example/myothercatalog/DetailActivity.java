package com.example.myothercatalog;

import android.content.Intent;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class DetailActivity extends AppCompatActivity {

    private TextView nombre; // Agregar un comentario sobre el propósito de este TextView
    private ImageView film; // Agregar un comentario sobre el propósito de esta ImageView
    private TextView description; // Agregar un comentario sobre el propósito de este TextView

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);

        // Aquí puedes agregar el código necesario para inicializar y mostrar los detalles de la película en la pantalla de detalles.
        // Por ejemplo, puedes obtener datos del Intent que inició esta actividad.

    }
}
