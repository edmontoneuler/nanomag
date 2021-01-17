def get_mag_arrays(filename, grid_dims):
    Nx, Ny, Nz = grid_dims[0], grid_dims[1], grid_dims[2]
    data = np.loadtxt(filename, delimiter = ',')
    
    raw_mx = data[0:Ny*Nz, :]
    raw_my = data[Ny*Nz:2*Ny*Nz, :]
    raw_mz = data[2*Ny*Nz:3*Ny*Nz,:] 
                  
    mx = np.zeros((Nx, Ny, Nz))
    my = np.zeros((Nx, Ny, Nz))
    mz = np.zeros((Nx, Ny, Nz))
                                
    for i in range(Nx):
        for j in range(Ny):
            for k in range(Nz):
                mx[i, j, k] = raw_mx[Ny*k+j, i]
                my[i, j, k] = raw_my[Ny*k+j, i]
                mz[i, j, k] = raw_mz[Ny*k+j, i]
                  
    return mx, my, mz

def xyplane_magplot(mx, my, mz, z_idx=0, grid_dims = (2,4,8), sample_dims = (2e-9,4e-9,8e-9), thinning = 1):
    
    Nx, Ny, Nz = grid_dims[0], grid_dims[1], grid_dims[2]
    Lx, Ly, Lz = sample_dims[0], sample_dims[1], sample_dims[2]
    x = np.linspace(0, Lx, Nx)
    y = np.linspace(0, Ly, Ny)
    
    X, Y = np.meshgrid(x,y)
    
    ### Choose appropriate XY plane (i.e. which )
    mx = mx[:, :, int(z_idx)].T
    my = my[:, :, int(z_idx)].T
    mz = mz[:, :, int(z_idx)].T
    
    fig = plt.figure()  
    
    Xthin = X[::thinning, ::thinning]
    Ythin = Y[::thinning, ::thinning]
    mxthin = mx[::thinning, ::thinning]
    mythin = my[::thinning, ::thinning]
    
    Q = plt.quiver(Xthin,Ythin,mxthin,mythin)
    I = plt.imshow(mz,extent=[np.min(X),np.max(X),np.min(Y),np.max(Y)], vmin=-1, vmax=1, origin ='lower', cmap='jet')
    
    plt.colorbar(cmap='jet')
    plt.show()
    
def xzplane_magplot(mx, my, mz, y_idx=0, grid_dims = (2,4,8), sample_dims = (2e-9,4e-9,8e-9), thinning = 1):
    
    Nx, Ny, Nz = grid_dims[0], grid_dims[1], grid_dims[2]
    Lx, Ly, Lz = sample_dims[0], sample_dims[1], sample_dims[2]
    x = np.linspace(0, Lx, Nx)
    z = np.linspace(0, Lz, Nz)
    
    X, Z = np.meshgrid(x,z)
    
    ### Choose appropriate XY plane (i.e. which )
    mx = mx[:, int(y_idx), :].T
    my = my[:, int(y_idx), :].T
    mz = mz[:, int(y_idx), :].T
    
    fig = plt.figure()  
    
    Xthin = X[::thinning, ::thinning]
    Zthin = Z[::thinning, ::thinning]
    mxthin = mx[::thinning, ::thinning]
    mzthin = mz[::thinning, ::thinning]
    
    Q = plt.quiver(Xthin,Zthin,mxthin,mzthin)
    I = plt.imshow(my,extent=[np.min(X),np.max(X),np.min(Z),np.max(Z)], vmin=-1, vmax=1, origin ='lower', cmap='jet')
    
    plt.colorbar(cmap='jet')
    plt.show()
    
    
def yzplane_magplot(mx, my, mz, x_idx=0, grid_dims = (2,4,8), sample_dims = (2e-9,4e-9,8e-9), thinning = 1):
    
    Nx, Ny, Nz = grid_dims[0], grid_dims[1], grid_dims[2]
    Lx, Ly, Lz = sample_dims[0], sample_dims[1], sample_dims[2]
    y = np.linspace(0, Ly, Ny)
    z = np.linspace(0, Lz, Nz)
    
    Y, Z = np.meshgrid(y,z)
    
    ### Choose appropriate XY plane (i.e. which )
    mx = mx[int(x_idx), :, :].T
    my = my[int(x_idx), :, :].T
    mz = mz[int(x_idx), :, :].T
    
    fig = plt.figure()  
    
    Ythin = Y[::thinning, ::thinning]
    Zthin = Z[::thinning, ::thinning]
    mythin = my[::thinning, ::thinning]
    mzthin = mz[::thinning, ::thinning]
    
    Q = plt.quiver(Ythin,Zthin,mythin,mzthin)
    I = plt.imshow(mx,extent=[np.min(Y),np.max(Y),np.min(Z),np.max(Z)], vmin=-1, vmax=1, origin ='lower', cmap='jet')
    
    plt.colorbar(cmap='jet')
    plt.show()
