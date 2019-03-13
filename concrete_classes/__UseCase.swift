//
//  __UseCase.swift
//  $_PROJECT_NAME
//
//  Created by $_AUTHOR on $_DATE.
//

import Foundation

class __UseCase {
    
    weak var presenter: __Presentable?
    let entityGateway: __EntityGatewayProtocol
    
    init(entityGateway: __EntityGatewayProtocol) {
        self.entityGateway = entityGateway
    }
    
}

// MARK: - __UseCaseProtocol
extension __UseCase: __UseCaseProtocol {
    
}
