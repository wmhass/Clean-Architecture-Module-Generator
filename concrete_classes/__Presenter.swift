//
//  __Presenter.swift
//  $_PROJECT_NAME
//
//  Created by $_AUTHOR on $_DATE.
//

import Foundation

class __Presenter {
    
    weak var view: __View?
    let useCase: __UseCaseProtocol
    let navigation: __Navigation
    
    init(useCase: __UseCaseProtocol, navigation: __Navigation) {
        self.useCase = useCase
        self.navigation = navigation
    }
    
}

// MARK: - __Presentable
extension __Presenter: __Presentable {
    
}

// MARK: - __ViewEventHandler
extension __Presenter: __ViewEventHandler {
    func viewDidLoad() {
        
    }
}
