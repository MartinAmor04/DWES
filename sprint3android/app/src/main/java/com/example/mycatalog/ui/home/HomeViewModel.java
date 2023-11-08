package com.example.mycatalog.ui.home;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

public class HomeViewModel extends ViewModel {

    private final MutableLiveData<String> mText;

    //Texto de la ventana principal
    public HomeViewModel() {
        mText = new MutableLiveData<>();
        mText.setValue("Esta es la ventana principal, accede a la barra superior izquierda para cambiar de ventana");
    }

    public LiveData<String> getText() {
        return mText;
    }
}