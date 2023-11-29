package com.example.myothercatalog;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

public class FilmViewHolder extends RecyclerView.ViewHolder {

    // Elementos de la vista de la celda
    private TextView name;
    private ImageView film;
    private Button button;

    // Constructor que recibe la vista de la celda e inicializa los atributos con los elementos de la misma.
    public FilmViewHolder(@NonNull View itemView) {
        super(itemView);
        name = itemView.findViewById(R.id.text_view_film);
        film = itemView.findViewById(R.id.image_view_film);
        button = itemView.findViewById(R.id.button);
    }

    /**
     * Método para mostrar los datos en la vista de la celda.
     *
     * @param filmData Datos de la película a mostrar.
     */
    public void showData(FilmData filmData) {
        name.setText(filmData.getName()); // Establecer el nombre de la película en el TextView
        Util.downloadBitmapToImageView(filmData.getImage_url(), this.film);

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Context context = v.getContext();
                Intent intent = new Intent(context, DetailActivity.class);

                // Aquí puedes agregar datos adicionales al intent, si es necesario.
                // Por ejemplo, puedes pasar el ID de la película para recuperar más detalles en la pantalla de detalles.

                context.startActivity(intent); // Iniciar la actividad de detalles
            }
        });
    }
}
