package com.example.myothercatalog;

import android.app.Activity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class FilmRecyclerViewAdapter extends RecyclerView.Adapter<FilmViewHolder> {

    private List<FilmData> films;
    private Activity activity;

    // Este es el constructor que recibe la lista de datos y la actividad asociada.
    public FilmRecyclerViewAdapter(List<FilmData> dataSet, Activity activity) {
        this.films=dataSet;
        this.activity=activity;
    }

    @NonNull
    @Override
    // El siguiente método es llamado cuando se necesita crear una nueva instancia de filmViewHolder
    public FilmViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        // La siguiente línea infla la vista del diseño de la celda y crea un nuevo filmViewHolder con esta.
        View filmView = LayoutInflater.from(parent.getContext()).inflate(R.layout.film_recycler_cell, parent, false);
        return new FilmViewHolder(filmView);
    }

    @Override
    // En este método siguiente, es llamado para actualizar el contenido de un filmViewHolder específico.
    public void onBindViewHolder(@NonNull FilmViewHolder holder, int position) {
        // Aquí obtenemos los datos correspondientes de la lista y llama al método showData en el filmViewHolder
        FilmData dataForThisCell = films.get(position);
        holder.showData(dataForThisCell);
    }

    @Override
    // En el siguiente método, devolvemos el número total de elementos en la lista de juegos.
    public int getItemCount() { return films.size(); }
}
