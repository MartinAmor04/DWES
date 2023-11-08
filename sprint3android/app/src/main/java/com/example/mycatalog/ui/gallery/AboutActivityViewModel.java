package com.example.mycatalog.ui.gallery;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

public class AboutActivityViewModel extends ViewModel {

    private final MutableLiveData<String> mText;

    //Instanciamos el texto que se ve en AboutActivity
    public AboutActivityViewModel() {
        mText = new MutableLiveData<>();
        mText.setValue("Para terminar quiero recomendar esta serie a todos los que disfruten de un anime interesante y con personajes elaborados. Neon Genesis Evangelion es una obra de anime que nació para la pantalla pequeña y que más adelante tuvo otros tipos de adaptaciones (manga, el reboot que fue Rebuild of Evangelion, etc). Como obra de anime su historia es excelente y creo que incluso 24 años después se mantiene igual de vigente. No es una obra perfecta pero por su casi nulo relleno y su corta duración es una entrega obligada para cualquier fanático del anime.");
    }

    public LiveData<String> getText() {
        return mText;
    }
}