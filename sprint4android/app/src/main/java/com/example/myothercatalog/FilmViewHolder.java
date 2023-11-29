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

    // Aquí nos encontramos los elementos de la vista de la celda
    private TextView name;
    private ImageView film;
    private Button button;

    // Este constructor recibe la vista de la celda e inicializa los atributos con los elementos de la misma.
    public FilmViewHolder(@NonNull View ivi) {
        super(ivi);
        name = ivi.findViewById(R.id.text_view_film);
        film = ivi.findViewById(R.id.image_view_film);


    }

    public void showData(FilmData filmData) {
        name.setText(filmData.getName()); // Establecemos el nombre del juego en el TextView
        Util.downloadBitmapToImageView(filmData.getImage_url(), this.film);
    }
}
