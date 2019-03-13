//
//  __Connector.swift
//  $_PROJECT_NAME
//
//  Created by $_AUTHOR on $_DATE.
//

import Foundation

class __Connector {
    
    func configure(view: __View) {
        let navigation = __Wireframe()
        let entityGateway = __EntityGateway()
        let useCase = __UseCase(entityGateway: entityGateway)
        let presenter = __Presenter(useCase: useCase, navigation: navigation)
        
        useCase.presenter = presenter
        presenter.view = view
        view.eventHandler = presenter
    }
    
}
